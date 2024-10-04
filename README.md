# Chess Bot

A Stockfish powered engine to play different openings

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)

## Introduction

The Chess Bot is a Python-based chess application that integrates the Stockfish 17 engine with Pygame, allowing users to practice and explore various chess openings. The bot loads PGN files to simulate different opening sequences, providing users with a dynamic learning environment. I chose to use PGN files instead of BIN files because PGN files are far more common and widely available. They are also simpler to use directly which eliminates the need to convert every single PGN file into the BIN format. By leveraging the existing library of PGN files, I can focus on integrating openings and strategies more efficiently. This bot is mainly for beginner and intermediate chess players to gain more opening move knowledge in a realstic manner but other players can benefit from refining their knowlegde too.  

## Features

Key Features Include:
- PGN File Integration: Users can load PGN files with pre-defined openings to practice different strategies.
- Opening Training: Players can select specific openings or let the bot decide for them.
- Interactive Chessboard: A visually appealing, interactive board built with Pygame for an intuitive gaming experience.

## Technologies Used

Built with: Python- pygame, Stockfish 17
