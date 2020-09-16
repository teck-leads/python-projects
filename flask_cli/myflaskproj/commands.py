from flask import Flask
import click
app = Flask(__name__)

@app.cli.command()
@click.argument('x')
@click.argument('y')
def power(x,y):
    try:
        p=1
        x=int(x)
        y=int(y)
        # result=pow(x, y)
        for i in range(y):
            p=p*x
        print(p)
    except ValueError:
            if(isinstance(x, str)):
                print('Error: Invalid value for "X"')
            elif(isinstance(y, str)):
                print('Error: Invalid value for "Y"')


@app.cli.command()
@click.argument('s')
@click.argument('n')
def repeat(s,n):

    try:
        result=""
        n=int(n)
        for i in range(n):
            result=result+s
        print(result)
        pass
    except ValueError:
            if(isinstance(n, str)):
                print('Error: Invalid value for "N"')
            


