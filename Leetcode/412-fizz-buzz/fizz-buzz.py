class Solution(object):
    def fizzBuzz(self, n):
        output=[]
        for i in range(1,n+1):
            if i%3==0:
                answer="Fizz"
                if i%5==0:
                    answer +="Buzz"
            elif i%5==0:
                answer="Buzz"
            else:
                answer=str(i)
            output.append(answer)
        return output


            