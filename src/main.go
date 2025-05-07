// ContactList - CTCL 2025
// File: src/main.go
// Purpose: Server definition
// Created: March 23, 2025
// Modified: May 6, 2025

package main

import (
	"log"
	"github.com/gin-gonic/gin"
	"strconv"
)

var config Config;
var logger *log.Logger = log.Default();

func main() {
	config, err := loadconfig("config/config.json");
	if err != nil {
		logger.Fatal(err);
	}

	router := gin.Default();
	router.GET("/", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "Hello, World!",
		});
	})
	router.Run(":" + strconv.Itoa(config.Port))


}