defmodule BubbleSort do
  def sort([]), do: []
  def sort([_]), do: [_]

  def sort(list) do
    bubbleSort(list, length(list))
  end

  defp bubbleSort(list, 0), do: list

  defp bubbleSort(list, n) do
    {new_list, _} =
      list
      |> Enum.with_index()
      |> Enum.reduce({[], nil}, fn
        {item, index}, {acc, prev} when index > 0 and prev > item ->
          {[item | acc], item}

        {item, index}, {acc, prev} when index > 0 ->
          {[prev | acc], item}

        {item, 0}, {acc, _} ->
          {[item | acc], item}
      end)
      |> then(fn {acc, last} -> {Enum.reverse([last | acc]), last} end)

    bubbleSort(new_list, n - 1)
  end
end
