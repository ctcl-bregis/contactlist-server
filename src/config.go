// ContactList - CTCL 2025
// File:config.go
// Purpose: Config definition and parsing
// Created: March 23, 2025
// Modified: May 6, 2025

package main

import (
	"encoding/json"
	
	"io"
	"os"
)

type Config struct {
	Bind string `json:"bind"`
	Port int    `json:"port"`
}


func loadconfig(path string) (Config, error) {
	jsondata, err := os.Open(path)
	if err != nil {
		return Config{}, err
	}
	defer jsondata.Close()

	byteValue, _ := io.ReadAll(jsondata)

	var config Config

	_ = json.Unmarshal(byteValue, &config)

	return config, nil
}