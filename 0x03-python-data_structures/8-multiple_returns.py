#!/usr/bin/python3


def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    strlength = len(sentence)
    firstchar = sentence[0]
    return (strlength, firstchar)
