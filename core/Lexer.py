class Lexer:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.stack = []
        self.var = {}
        
        
    def error(self, msg: str) -> str:
        print(f'ERROR: {msg}')
    
    
    def get_value(self, var: str) -> int | float | str:
        try:
            return self.var.get(var)
        except:
            self.error(f'\'{var}\' is not declared.')
        
        
    def analyze(self, rows: list[str]) -> str:
        for row in rows:
            for token in row.split():
                match token:
                    case '+':
                        a = self.stack.pop()
                        b = self.stack.pop()
                        try:
                            self.stack.append(float(self.get_value(b)) + float(self.get_value(a)))
                        except:
                            self.stack.append(b + a)
                    case '-':
                        a = self.stack.pop()
                        b = self.stack.pop()
                        try:
                            self.stack.append(float(self.get_value(b)) - float(self.get_value(a)))
                        except:
                            self.stack.append(b - a)
                    case '*':
                        a = self.stack.pop()
                        b = self.stack.pop()
                        try:
                            self.stack.append(float(self.get_value(b)) * float(self.get_value(a)))
                        except:
                            self.stack.append(b * a)
                    case '/':
                        a = self.stack.pop()
                        b = self.stack.pop()
                        try:
                            self.stack.append(float(self.get_value(b)) / float(self.get_value(a)))
                        except:
                            self.stack.append(b + a)
                    case '=':
                        value = self.stack.pop()
                        name = self.stack.pop()
                        self.var.update({f"{name}":f"{value}"})
                    case '.':
                        try:
                            print(self.stack[-1])
                        except:
                            self.error('the stack is empty!')
                    case '$':
                        self.var.update({f"{self.stack.pop()}":f"{input()}"})
                    case _:
                        try:
                            self.stack.append(float(token))
                        except:
                            if token in self.var.keys():
                                self.stack.append(float(self.var.get(token)))
                            else:
                                self.stack.append(token)
                
    
    
    def read_file(self) -> str | None:
        try:
            with open(self.filename, 'r') as f:
                Lexer.analyze(self, f.read().splitlines())
                f.close()
        except Exception as e:
            print(f'ERROR: {e}')
