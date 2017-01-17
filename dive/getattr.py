#!/usr/bin/env python
# coding=utf-8

import statsout

def output(data, format="text"):
    output_function = getattr(statsout, "output_%s" % format, statsout.output_text)
    return output_function(data)

if __name__ == "__main__":
    output("hp", "pdf");
