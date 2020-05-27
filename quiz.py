import pandas as pd

def calulate_final_score(i):

    return ('The final score is '+str(2*i))


df = pd.read_csv("problems.csv", names=['Question','Answer'])
df['Answer'].to_dict

for i in range(len(df)):
    print('The '+ str() +'th question is')
    print(df['Question'][i])
    ans = int(input( "Enter the answer"))
    print(type(ans))
    if ans == df['Answer'][i]:
        print('Correct')
    else:
        print('Incorrect')
        i -= 1
        break

print(calulate_final_score(i+1))
