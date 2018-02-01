class Parser:
    def __init__(self, filepath):
        self.file = open(filepath, 'r+')

    def parse (self):
        commands = []
        action = []
        for line in self.file:
            line = line.replace('\n', ' ')
            line = line.split(' : ')
            commands.append(line[0])
            action.append(line[1])
        self.setCommands(commands)

    def setCommands(self,commandsArray):
        self.commands = commandsArray

    def getCommands(self):
        return self.commands

    def setActions(self,actionsArray):
        self.actions = actionsArray

    def getActions(self):
        return self.actions

app = Parser('commands.lib')
app.parse()
for command in app.getCommands():
    print(command)
