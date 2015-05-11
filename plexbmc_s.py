import sys
import time

plexbmc_start = time.time()
print "===== PlexBMC START [id: %s] =====" % plexbmc_start
print " >> PlexBMC Processing request: [%s] =====" % sys.argv

from resources.lib.commands import COMMANDS, BaseCommand

command_name = sys.argv[1]
args = sys.argv[2:]

command = COMMANDS.get(command_name)
if command and issubclass(command, BaseCommand):
    print "executing command: %s; with args: %s" % (command, args)
    command(*args).execute()

print "===== PlexBMC STOP [id: %s]: %s seconds =====" % (plexbmc_start, (time.time() - plexbmc_start))
sys.modules.clear()