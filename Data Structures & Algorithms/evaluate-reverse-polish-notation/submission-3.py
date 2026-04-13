class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_queue = []

        for i in range(len(tokens)):
            token = tokens[i]
            if token in '+-*/':
                numr = num_queue.pop()
                numl = num_queue.pop()
                if token=='+':
                    tmp = numl+numr
                elif token=='/':
                    print(f'{numl}//{numr}')
                    tmp = int(numl/numr)
                elif token=='-':
                    tmp = numl-numr
                else:
                    tmp = numl*numr
                num_queue.append(tmp)
                print(tmp)
            else:
                num_queue.append(int(token))
        return num_queue.pop()
            

