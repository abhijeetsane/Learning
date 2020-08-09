package main

import (
	"fmt"
	"net/http"
)

func loop_http_handler(w http.ResponseWriter, r *http.Request) {
	fmt.Println(r.UserAgent())
	for i := 0; i < 10; i++ {
		fmt.Fprintf(w, "(%d) : Hello  Abhijeet !", i)
	}
	fmt.Fprintf(w, "Hello, %s!", r.URL.Path[1:])
}
