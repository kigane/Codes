import math
import json

class JsonLike:
    def __init__(self, json) -> None:
        self._data = json

    def __getattr__(self, name):
        return self._data[name]
    
    def __getitem__(self, name):
        return self._data[name]

with open('base/plays.json', 'r') as p:
    plays = json.load(p, object_hook=JsonLike)

with open('base/invoices.json', 'r') as inv:
    invoices = json.load(inv, object_hook=JsonLike)


def statement(invoice, plays):
    totalAmount = 0
    volumeCredits = 0
    result = f'Statement for { invoice.customer }\n'
    format = lambda x: f'${x:,.2f}'

    for perf in invoice.performances:
        play = plays[perf.playID]
        thisAmount = 0

        if play.type == "tragedy":
            thisAmount = 40000
            if perf.audience > 30:
                thisAmount += 1000 * (perf.audience - 30)
        elif play.type == "comedy":
            thisAmount = 30000
            if perf.audience > 20:
                thisAmount += 10000 + 500 * (perf.audience - 20)
            thisAmount += 300 * perf.audience
        else:
            raise ValueError(f'unknown type: {play.type}')

        # add volume credits
        volumeCredits += max(perf.audience - 30, 0)
        # add extra credit for every ten comedy attendees
        if ("comedy" == play.type): volumeCredits += math.floor(perf.audience / 5)

        # print line for this order
        result += f'  {play.name}: {format(thisAmount/100)}({perf.audience} seats)\n'
        totalAmount += thisAmount
    
    result += f'Amount owed is {format(totalAmount/100)}\n'
    result += f'You earned {volumeCredits} credits\n'
    return result

if __name__ == '__main__':
    print(statement(invoices[0], plays))
