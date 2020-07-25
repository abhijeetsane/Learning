defmodule Maths do
  def add(x , y) when is_integer(x) and  is_integer(y)  and not is_atom(x) and not is_atom(y) do
    x + y
  end
end
