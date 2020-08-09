package main

import (
	"fmt"
	"net/http"
)

func main() {
	fmt.Println("%s\n", "Starting the GoLang Default HTTP Server")
	http.HandleFunc("/", HelloServer)
	http.HandleFunc("/loop/", loop_http_handler)
	http.ListenAndServe(":8080", nil)
}

func HelloServer(w http.ResponseWriter, r *http.Request) {
	fmt.Println(r.UserAgent())
	fmt.Fprintf(w, "Hello, %s!", r.URL.Path[1:])
}
