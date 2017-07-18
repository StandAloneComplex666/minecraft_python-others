
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()
def safeFeet():
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x, pos.y-1, pos.z)
    c = mc.getBlock(pos.x, pos.y, pos.z)
    if b == block.AIR.id or c == block.WATER_STATIONARY.id or c == block.WATER_FLOWING.id:
        mc.postToChat("Help!I am not safe")
    else:
        mc.postToChat("Safe,my friend")

def buildbridge():
    pos  =mc.player.getTilePos()
    b = mc.getBlock(pos.x, pos.y-1, pos.z)
    if  b == block.WATER_FLOWING.id or b == block.WATER_STATIONARY.id:
        mc.setBlock(pos.x, pos.y-1, pos.z, block.GLASS.id)
while True:
    time.sleep(0.1)
    safeFeet()
    buildbridge()