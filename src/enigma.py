import enigmalogic as logic

###Input Types:
Id=str
Li=list
###Parsing:
def parse(program):
    #read expression
    return Read_Token(tokenize(program))

def tokenize(line):
    return line.replace('(',' ( ').replace(')',' ) ').split()

def Read_Token(tokens):
    L=[]
    for token in tokens:
            L.append(token)
    return L
    
###Environment:
def Std_Environment():
    #Enviroment with standard procedures:
    env=Env()
    # env.update({
    #     'len':  len, 
    #     #'list':    lambda *x: list(x), 
    #     #'isList':   lambda x: isinstance(x,list), 
    #     '?Null':   lambda x: x == [], 
    #     'isValid': lambda x: isinstance(x, Id),
    #     'input' : lambda prompt: input(prompt),
    #     '?='   :opLogic.eq,
    # })    
    return env
    
class Env(dict):
    def __init__(self, parms=(), args=(), outer=None):
        self.update(zip(parms, args))
        self.outer = outer
    def find(self, var):
        return self if var in self else self.outer.find(var)


global_env = Std_Environment()    

### Interaction: A REPL
def repl(prompt='enigma.py> '):
    #A prompt-read-eval-print loop.
    while True:
        val = eval(parse(input(prompt)))
        if val is not None: 
            print(inputStr(val))

def inputStr(exp):
    #Convert a Python object back into a readable string.
    if isinstance(exp, Li):
        return ''.join(map(inputStr, exp))
    else:
        return str(exp)

class Procedure(object):
    "A user-defined Scheme procedure."
    def __init__(self, parms, body, env):
        self.parms, self.body, self.env = parms, body, env
        
    def __call__(self, *args): 
        # Create a new environment for the procedure call, inheriting from the procedure's environment
        procedure_env = Env(self.parms, args, self.env)
        
        # Evaluate the body of the procedure in the new environment
        return eval(self.body, procedure_env)
################ eval
curCode=[0]
curState=[]
def eval(x, env=global_env):
    global curCode
    global curState
    #Evaluate an expression in an environment.
    if isinstance(x, Id):      # variable reference
        found= env.find(x)
        if found is not None:
            return found[x]
    elif not isinstance(x, Li):  # constant literal
        return str(x) 
    
    elif x[0]=="if":
        ifStmt=str(' '.join(x))
        if "else" in x:
            stmts1, stmts2 =ifStmt.split("else",1)
        else: 
            stmts1=x
        condition, expr=''.join(stmts1).split('|')
        condition=condition.replace("if",'')
        if eval(parse(condition))==True:
                eval(parse(expr))
        else:
                eval(parse(stmts2))

    elif x[0]=="do" :
        loop=str(' '.join(x))
        stmts, condition =loop.split("while",1)
        stmts=stmts.replace("do",'',1)
        stmt=stmts.split(',')
        stmt.pop() 
        #print (stmt)
        for element in stmt:
                #print(element)
                eval(parse((element)))
        while eval(parse(condition))==True:
            for element in stmt:
                eval(parse((element)))

    elif "then" in x:
        arg1, arg2 =str(' '.join(x)).split("then",1)
        exp1=arg1.split()
        if exp1:
            eval(exp1)
        exp2=arg2.split()
        if exp2:
            eval(exp2)

    elif x[0] == "set":
        curCode=[]
        if x[1]=='(' and x[3]==')':
            code=''.join(str(eval(str(x[2]))))
            curCode=logic.Gen_Code(code)
        else:
            code = ''.join(x[1:])
            curCode=logic.Gen_Code(code)
        curState=[]
        curState=curCode.copy()

    elif x[0]=="save":
        if len(x)==4:
            msg=curState.copy()
        else:
            msg=' '.join(x[4:])
        if x[1]=='(' and x[3]==')':
            env[str(x[2])]=msg
        else:
            raise SyntaxError ('wrong format') 
        
    elif x[0]=="update":
        curState=[]
        if x[1]=='(' and x[3]==')':
            msg=eval(str(x[2]))
            curState=msg
        else:
            msg=' '.join(x[1:])
            curState=msg
        return curState

    elif x[0]=="encode":
        curMsg=[]
        curMsg=curState
        curState=[]
        if len(x)==2:
            if x[1]=="cae":
                curState=logic.Caesar_Encrypt(curMsg,curCode)
            elif x[1]=="lay":
                curState=logic.Layer_Encrypt(curMsg,curCode)
        else:
            if x[2]=='(' and x[4]==')':
                curMsg=eval(str(x[3]))
                if x[1]=="cae":
                    curState=logic.Caesar_Encrypt(curMsg,curCode)
                elif x[1]=="lay":
                    curState=logic.Layer_Encrypt(curMsg,curCode)
            else:
                raise SyntaxError ('wrong format')
        return curState
            
    elif x[0]=="decode":
        curMsg=[]
        curMsg=curState
        curState=[]
        if len(x)==2:
            if x[1]=="cae":
                curState=logic.Caesar_Decrypt(curMsg,curCode)
            elif x[1]=="lay":
                curState=logic.Layer_Decrypt(curMsg,curCode)
        else:
            if x[2]=='(' and x[4]==')':
                curMsg=eval(str(x[3]))
                if x[1]=="cae":
                    curState=logic.Caesar_Decrypt(curMsg,curCode)
                elif x[1]=="lay":
                    curState=logic.Layer_Decrypt(curMsg,curCode)
            else:
                raise SyntaxError ('wrong format')
        return curState

    elif x[0]=="pr":
        if len(x)<2:
            logic.Print_Msg(curState)
        elif x[1]=='(' and x[3]==')':
            try:
                if x[2]=="?state":
                    logic.Print_Msg(curCode)
                    logic.Print_Msg(curState)
                elif x[2]=="?rule":
                    print(logic.tempRules)
                else:
                    print(eval(x[2]))
            except:
                raise SyntaxError ("variable not found")
        else:
            msg=' '.join(x[1:])
            print (msg)
            
    elif x[0]=="open":
        if x[1]=='(' and x[3]==')':
            try:
                path=eval(str(x[2]))
            except:
                path=str(x[2])
            curState=[]
            curState=logic.Read_File(path)
            return curState
    
    elif x[0]=="export":
        if x[1]=='(' and x[3]==')':
            try:
                path=eval(str(x[2]))
            except:
                path=str(x[2])
            return logic.Write_File(path, curState)

    elif x[0]=="rule":
        L={}
        x.pop(0)
        element=''.join(x).split(',')
        for i in element:
            L.update(logic.To_Dict(str(i)))
        logic.Set_Rule(L)

    elif x[0]=="reset":
        logic.Reset_Rule()

    elif x[0]=="ask":
        if x[1]=='(' and x[3]==')':
            user=0
            user=str(x[2])
            env[user]=input()
        else: 
            raise SyntaxError ('Wrong format')
        
    elif x[0]=="run":
        s=[]
        if x[1]=='(' and x[3]==')':
            try:
                path=eval(str(x[2]))
            except:
                path=str(x[2])
        with open(path, 'r') as f:
            allLine=""
            for line in f:
                allLine+=line.replace('\n',' ')
            # print(allLine)
            stmts=allLine.split(';')
            stmts.pop()
            # print(stmts)
            for stmt in stmts:
                eval(parse(stmt))

    elif x[0] == "define":
        var=x[1]
        parms=[]
        if x[2]=='(' and x[4]==')':
            parms=x[3]
        body=x[5:]
        print (var, parms, body)
        parms="123"
        eval(body)
    elif x[0]=="compare":
        if x[1]=='(' and x[3]==')':
            try:
                var1=eval(str(x[2]))
            except:
                var1=x[2]
        exp=x[4:]
        condition=var1+"".join(exp)
        return logic.compare(condition)
        
    else:
        # return proc(*args)
        print("No instruction found")

repl()