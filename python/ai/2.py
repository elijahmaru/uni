import random
from typing import Tuple
import matplotlib.pyplot as plt


class vacuumWorld:
    def __init__(self, initialDirty: Tuple[bool, bool, bool], agentPos: int = 0):
        """
        initial_dirty: tuple (dirty_A, dirty_B) - True если грязно
        agent_pos: 0 for A, 1 for B
        """
        self.cells = [
            bool(initialDirty[0]),
            bool(initialDirty[1]),
            bool(initialDirty[2]),
        ]
        self.agentPos = agentPos  # 0 = A, 1 = B

    def getPercept(self) -> Tuple[str, str]:
        loc = "A"
        match self.agentPos:
            case 0:
                loc = "A"
            case 1:
                loc = "B"
            case 2:
                loc = "C"
            case _:
                raise ValueError("Unknown position")
        status = "Dirty" if self.cells[self.agentPos] else "Clean"
        return loc, status

    def applyAction(self, action: str):
        match action:
            case "Suck":
                self.cells[self.agentPos] = False
                if random.random() < 0.2:
                    self.cells[random.randrange(0, 3)] = True
            case "Right":
                self.agentPos += 1
                if random.random() < 0.2:
                    self.cells[random.randrange(0, 3)] = True
            case "Left":
                self.agentPos -= 1
                if random.random() < 0.2:
                    self.cells[random.randrange(0, 3)] = True
            case "NoOp":
                if random.random() < 0.2:
                    self.cells[random.randrange(0, 3)] = True
        pass

    def getState(self):
        return {
            "A": "Dirty" if self.cells[0] else "Clean",
            "B": "Dirty" if self.cells[1] else "Clean",
            "C": "Dirty" if self.cells[2] else "Clean",
            "agent_pos": (
                "A" if self.agentPos == 0 else "B" if self.agentPos == 1 else "C"
            ),
        }

    def reward(self, mode="per_cell") -> float:
        """mode: 'per_cell' -> +1 per clean cell (0..2)
        'both_clean' -> +1 if both clean else 0"""
        if mode == "per_cell":
            return (
                (0 if self.cells[0] else 1)
                + (0 if self.cells[1] else 1)
                + (0 if self.cells[2] else 1)
            )
        elif mode == "all_clean":
            return (
                1.0
                if (not self.cells[0] and not self.cells[1] and not self.cells[2])
                else 0.0
            )
        else:
            raise ValueError("Unknown reward mode")


class smartAgent:
    def act(self, percept: Tuple[str, str], lastAction: str) -> str:
        loc, status = percept
        if status == "Dirty":
            return "Suck"
        elif loc == "B" and lastAction == "Left":
            return "Left"
        return "Left" if loc == "C" else "Right"


class randomAgent:
    def act(self, percept: Tuple[str, str]) -> str:
        loc, status = percept
        if status == "Dirty" and loc == "C":
            return "Go to A"
        elif loc != "B":
            return "Left" if loc == "C" else "Right"
        return "Left" if bool(random.getrandbits(1)) else "Right"


def simulateSmart(
    world: vacuumWorld, agent: smartAgent, steps: int = 10, reward_mode="per_cell"
):
    log = []
    total_reward = 0.0
    lastAction = "NoOp"
    for t in range(steps):
        percept = world.getPercept()
        action = agent.act(percept, lastAction)
        world.applyAction(action)
        r = world.reward(mode=reward_mode)
        total_reward += r
        lastAction = action
        log.append(
            {
                "step": t,
                "percept": percept,
                "action": action,
                "state": world.getState(),
                "reward": r,
            }
        )
    return log, total_reward


def simulateRand(
    world: vacuumWorld, agent: randomAgent, steps: int = 10, reward_mode="per_cell"
):
    log = []
    total_reward = 0.0
    for t in range(steps):
        percept = world.getPercept()
        action = agent.act(percept)
        world.applyAction(action)
        r = world.reward(mode=reward_mode)
        total_reward += r
        log.append(
            {
                "step": t,
                "percept": percept,
                "action": action,
                "state": world.getState(),
                "reward": r,
            }
        )
    return log, total_reward


def compareAgents(steps: int = 10, runs: int = 50):
    agents = {"smartAgent": smartAgent(), "randomAgent": randomAgent()}
    results = {}
    initDirty = []
    for fst in (True, False):
        for snd in (
            True,
            False,
        ):
            for trd in (True, False):
                for i in range(0, 3):
                    initDirty.append(((fst, snd, trd), i))
    print(initDirty)
    for name, agent in agents.items():
        avgRewards = [0.0] * steps
        for i in range(runs):
            world = vacuumWorld(initDirty[i % 24][0], agentPos=initDirty[i % 3][1])
            if name == "smartAgent":
                log, total = simulateSmart(world=world, agent=agent, steps=steps)
            else:
                log, total = simulateRand(world=world, agent=agent, steps=steps)
            rewardsPerStep = [entry["reward"] for entry in log]
            avgRewards = [a + b for a, b in zip(avgRewards, rewardsPerStep)]
        avgRewards = [x / runs for x in avgRewards]
        results[name] = avgRewards

    plt.figure(figsize=(10, 5))
    for name, rewards in results.items():
        plt.plot(range(steps), rewards, label=name)
    plt.xlabel("Step")
    plt.ylabel("Avg reward")
    plt.title(f"Avg reward per step (runs={runs})")
    plt.legend()
    plt.grid(True)
    plt.show()
    print("График выведен")
    for name, rewards in results.items():
        print(f"{name}: Средний reward за шаг = {sum(rewards) / len(rewards):.3f}")


if __name__ == "__main__":
    inits = []
    for fst in (True, False):
        for snd in (
            True,
            False,
        ):
            for trd in (True, False):
                for i in range(0, 3):
                    inits.append(((fst, snd, trd), i))
    for initial_dirty, pos in inits:
        wordSmart = vacuumWorld(initial_dirty, agentPos=pos)
        agentSmart = smartAgent()
        wordRand = vacuumWorld(initial_dirty, agentPos=pos)
        agentRand = randomAgent()
        logSmart, totalSmart = simulateSmart(
            wordSmart, agentSmart, steps=10, reward_mode="per_cell"
        )
        logRand, totalRand = simulateRand(
            wordRand, agentRand, steps=10, reward_mode="per_cell"
        )
        print(
            "Init:",
            initial_dirty,
            "start:",
            "A" if pos == 0 else "B" if pos == 1 else "C",
        )
        print("Smart agent")
        for entry in logSmart:
            print(entry, "\n")
        print("Total reward:", totalSmart, "\n")
        print("Random agent")
        for entry in logRand:
            print(entry, "\n")
        print("Total reward:", totalRand)
        print("=" * 40, "\n")
    compareAgents()
