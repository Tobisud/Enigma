##### Enigma
#### Introduction:
The idea of encoding and decoding is simply that we move the order of the
letters in the alphabet. This programming language mainly helps you build an
encryption or decryption tool quickly. There are two ways to arrange numbers:
Caesar style and Layer style.

Caesar: you simply move each letter in a certain order
For example, if you have abcd and 123, the moving order is a->1, b->2, c->3,
d->1 respectively.

Layer: you also move each letter in a certain order but the numbers are arranged
more complicatedly.
For example, if you have abcd and 123, the order of moves is a->1, b->1+2=3,
c->1+2+3=6, d->1+2+3+1 =7.

The password can be a number or letter, the letters will be converted into order
according to a rule (pre-arranged dictionary) A->Z:1->26 and a->z:27->52. You
can change this order to suit each person using the “rule” command.

In this programming language, I want to optimize and simplify programming by
reducing things like calling variables or naming variables. You can still do it the
traditional way, but it also provides a shortcut. There are two global variables:
curCode and curState. curCode is the code you use for encoding or decoding
and curState will remember the last text you entered or read (text, not code). This
makes it easy to create a quick and efficient encryption or decryption tool (example 2).
By reading or entering a text, curState will remember it and you can then use pr (print) or
encode without needing to call any additional variable names.

All the encode and decode login store in separate file call “enigmalogic” and
import to the interpreter.

#### Syntax:
Keyword:
1. “if” for if statement: if condition | statements
2. “do-while” for while statement: do statements while condition
3. “then” same as and
4. “set” set passcode
5. “save” same as assign
6. “update” update a string to the current state
7. “encode cae” encode message - Caesar style
8. “encode lay” encode message - Caesar style
9. “decode cae” decode message - Layer style
10. “decode lay” decode message - Layer style
11. “pr” short for print
12. “open” open a file
13. “export” copy texts to a file
14. “rule” update your rules
15. “reset” reset rule
16. “ask” ask user for input
17. “run” execute a .egi file
18. “compare” use for compare variable
19. “?state” check the curCode and curState
20. “?rule” check the current rule

#### Declare, refer variables & special rules:
All variables should be put in ( ) otherwise it will read as string.
Example: pr hello output: hello
save (hello) abc; pr (hello); output: abc
All statements must end with ‘;’ except while loop.
Statements inside loop end with ‘,’
