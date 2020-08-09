defmodule HttpClient do
  def get_home_page do
    HTTPoison.start
    case HTTPoison.get("http://httparrot.herokuapp.com/get") do
      {:error , reason} -> IO.puts("Error has occred  #{reason}")
      {:ok , %HTTPoison.Response{status_code: 200, body: body} } -> 
        for {k ,v } <- body do
          IO.puts("#{k} => #{v}")  
        end
        IO.puts(is_bitstring(body))
        IO.puts("Connection worked ")
    end  
  end
  {:ok , "Application for Http Client"}
end 
