// ContactList - CTCL 2025
// File: src/main.go
// Purpose: Server definition
// Created: March 23, 2025
// Modified: March 23, 2025

package main

import (
	//"html/template"
	"net/http"
	//"path/filepath"

	"log"

	"github.com/go-chi/chi/v5"
	//"github.com/go-chi/chi/v5/middleware"
)

var config = loadconfig("config/config.json")
var logger = log.Default()

func main() {
	r := chi.NewRouter()

	bind := config.Bind+":"+string(rune(config.Port))

	err := http.ListenAndServe(bind, r)
	if err != nil {
		panic(err)
	} else {
		logger.Println("Server started bound to " + bind)
	}
}