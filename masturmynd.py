# Copyright (c) 2015 Philipp Nowak (https://xxyy.github.io)
# See the file LICENSE for copying permission.

import sys
import re

# http://www.linuxhowtos.org/Tips%20and%20Tricks/ansi_escape_sequences.htm
COL_YELLOW_BOLD = "\033[1;33m"
COL_WHITE_BOLD  = "\033[1;37m"
COL_CYAN_BOLD   = "\033[1;36m"
COL_RED_BOLD    = "\033[1;31m"
COL_NORMAL      = "\033[0;37m"
COL_RESET       = "\033[0m"

def check(inp, sol):
  """Check an input string against a solution string, returning a human-readable
  message as output, detailing either the results or an error message."""
  if len(inp) != len(sol):
    return "!Invalid length (Required: %s)" % len(sol)
  black,white = 0,0
  fuzzy = set(inp)
  
  for i in range(0,len(sol)):
    subj = inp[i]
    if subj == sol[i]:
      black += 1
      if subj in fuzzy:
        fuzzy.remove(subj)
  
  white = len(fuzzy & set(sol))
  return "%sW%sB" % (white, black)

def notice(msg):
  """Print an important notice with asterisks for attention in color."""
  print("%s ***%s %s %s" % (COL_YELLOW_BOLD, COL_WHITE_BOLD, msg, COL_NORMAL))

def message(msg):
  """Print a normal message, making parts in single quotes in color."""
  print(re.sub(r"'([^']+)'", COL_RESET + r"\1" + COL_NORMAL, msg));

def format_output(out):
   """Format a human-readable output, as returned by check(inp, sol).
   
   Return False if an error message was detected."""
  if out.startswith("!"):
    print("  %s! %s%s%s" % (COL_RED_BOLD, COL_NORMAL, out[1:], COL_RESET))
    return False
  else:
    print("%s  %s" % (COL_NORMAL, out))
    return True




notice("Welcome to Mastur Mynd")
notice("Type 'help' for help")

while True:
  cmd=input("\n%sλ %s" % (COL_CYAN_BOLD, COL_RESET))
  print(COL_NORMAL)
  
  if cmd == "help":
    message("  'Mastur Mynd' is a game where you have to\n" +
             "  make up a string and your opponent has\n" +
             "  to guess it. \n" +
             "\n" +
             "  If they guess a character right, it is\n" +
             "  '\"black\" (B)', if a character is in the\n" +
             "  string, but not at the correct position,\n" +
             "  it is '\"white\" (W)'. They get the amount\n" +
             "  of matches in the form '#W#B' and have\n" +
             "  to continue guessing until they find\n" +
             "  the solution.\n" +
             "\n" +
             "  Type 'start' to start a game.\n" +
             "\n" +
             "  Have fun!")
  elif cmd == "start":
    attempts = 1
    sol=input("  Solution: " + COL_RESET)
    correct_out = "0W%sB" % len(sol)
    out=""
      # Replace previous line to hide solution:
    sys.stdout.write("\033[F\033[2K")

    while out != correct_out:
      inp = input("%s  %d|%s" % (COL_NORMAL, attempts, COL_RESET))
      out = check(inp, sol)
      if format_output(out): # returns True if successful attempt
        attempts += 1 
    
    print("  gg\n") # good game
    notice("Game finished with %d attempts." % (attempts - 1))
    notice("Type 'quit' to close the program.") 
  elif cmd == "quit":
    print("  Thanks for playing!" + COL_RESET)
    exit(1)
  else:
    print("Unknown command. Type 'help' for help.")
