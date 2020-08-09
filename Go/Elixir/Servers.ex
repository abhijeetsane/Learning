defmodule Servers  do

  def startEchoServer() do
    spawn(fn-> EchoServer.start(5555) end)
  end
end
