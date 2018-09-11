"""  Given a String of length N reverse the whole string without reversing the individual words in it.
 Words are separated by dots.

Input:
The first line contains T denoting the number of testcases. Then follows description of testcases.
 Each case contains a string containing spaces and characters.


Output:
For each test case, output a single line containing the reversed String.

Constraints:
1<=T<=20
1<=Lenght of String<=2000


Example:
Input:
2
i.like.this.program.very.much
pqr.mno

Output:
much.very.program.this.like.i
mno.pqr """


for _ in range(int(input())):
    s = input().split('.')

    print('.'.join(s[::-1]))
