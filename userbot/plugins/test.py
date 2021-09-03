from uniborg.util import VAMPBOT_cmd


@borg.on(VAMPBOT_cmd(pattern=r"test"))
async def test(event):
    if event.fwd_from:
        return
    await event.edit("Test Successfull. Boss !")
