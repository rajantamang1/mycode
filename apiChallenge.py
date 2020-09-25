
"""api challenge | Author:Rajan Tamang"""
import requests

result = requests.get("https://cat-fact.herokuapp.com/facts").json()
def nameAll():

    listName =[]
    for name in result['all']:
        listName.append(f"{name['user']['name']['first']} {name['user']['name']['last']}")
        for names in listName:

            print(f"All the writers we have:", names)
def main():

    #print(result.json())

    nameAll()

main()