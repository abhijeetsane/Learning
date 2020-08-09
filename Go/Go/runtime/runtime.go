package main
import "fmt"
import "runtime"

func main() {
    num_of_proc :=  runtime.NumCPU()
    num_of_co_routines := runtime.NumGoroutine()
    fmt.Printf("Go Lang Version : %s\n" , runtime.Version())
    fmt.Printf("Number of Logical Processors : %d\n" , num_of_proc)
    fmt.Printf("Number of Goroutines : %d\n" , num_of_co_routines)
}
