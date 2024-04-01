import sys
sys.path.append(r"C:\Users\ACER\Desktop\File C\HarmonyHub\Function")
from DAL import DataAccess
import asyncio
from GUI import gui
# main.py

# if __name__ == "__main__":
#     app = gui.Presentation()
#     app.run()

async def main():
    dal = DataAccess()
    song = await dal.get_song()
    print(song)

asyncio.run(main())    