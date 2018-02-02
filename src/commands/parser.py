#!/usr/bin/env python3

class Parser:
    def __init__(self, filepath):
        self.file = open(filepath, 'r+')

    def parse (self):
        commands = []
        actions = []
        for line in self.file:
            if not line.startswith('#'): # Alow us to comment lines
                line = line.replace('\n', ' ')
                line = line.split(' <> ')
                commands.append(line[0])
                actions.append(line[1])
        self.setCommands(commands)
        self.setActions(actions)

    def setCommands(self,commandsArray):
        self.commands = commandsArray

    def getCommands(self):
        return self.commands

    def setActions(self,actionsArray):
        self.actions = actionsArray

    def getActions(self):
        return self.actions

