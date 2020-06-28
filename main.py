import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("OH MY GIRL Bot Ready")
    game = discord.Game("!도와줘")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!오마이걸 공식 트위터"):
        embed = discord.Embed(title="오마이걸 공식 트위터", url="https://twitter.com/WM_OHMYGIRL", description="@WM_OHMYGIRL",
                              color=0xff97fd)
        await message.channel.send(embed=embed)
    if message.content.startswith("!오마이걸 멤버"):
        embed = discord.Embed(title="오마이걸 멤버", url="https://bit.ly/31ndIEm", description="총 7명", color=0xfeb1eb)
        embed.add_field(name="김미현 (미미)", value="메인 랩퍼│1995년 5월 1일 (25세)│제주특별자치도 제주시", inline=False)
        embed.add_field(name="유시아 (유아)", value="리드 보컬│1995년 9월 17일 (24세)│서울특별시 용산구 신찬동", inline=False)
        embed.add_field(name="현승희 (승희)", value="리드 보컬│1996년 1월 25일 (24세)│강원도 춘천시 신북읍", inline=False)
        embed.add_field(name="김지호 (지호)", value="리드 보컬│1997년 4월 4일 (23세)│충청북도 옥천군", inline=False)
        embed.add_field(name="배유빈 (비니)", value="서브 보컬│1997년 9월 9일 (22세)│강원도 춘천시", inline=False)
        embed.add_field(name="최예원 (아린❤)", value="서브 보컬❤│1999년 6월 18일 (21세)│부산광역시 남구 용호동", inline=False)
        embed.add_field(name="최효정 (효정)", value="리더, 메인 보컬│1994년 7월 28일 (25세)│경기도 안양시", inline=False)
        embed.add_field(name="진이", value="거식증으로 인한 탈퇴│1995년 1월 22일 (25세)│경상북도 포항시", inline=False)
        embed.set_footer(text="출처: 나무위키 + Google")
        await message.channel.send(embed=embed)
    if message.content.startswith("!도와줘"):
        embed = discord.Embed(title="OH MY GIRL", description="!오마이걸, !오마이걸 데뷔일, !오마이걸 멤버, !오마이걸 노래 모음, !오마이걸 공식 트위터, !오마이걸 인스타, !오마이걸 멤버", color=0xff97fc)
        embed.set_author(name="명령어 목록 (거의 다 사용 불가능)")
        embed.add_field(name="명령어", value="!노래, !청소, !조용, !강퇴, !차단", inline=False)
        embed.add_field(name="베타 테스트", value="명령어는 계속해서 추가할 예정", inline=False)
        await message.channel.send(embed=embed)
    if message.content.startswith("!오마이걸 데뷔일"):
        embed = discord.Embed(title="오마이걸 데뷔일", description="오마이걸 데뷔일은 2015년 4월 20일입니다.", color=0xff99fd)
        await message.channel.send(embed=embed)

client.run("NzI2NjYxNzQ3MTcxMTMxNTEx.Xvi4RA.JsM4PKQ5kcqEfoCjh5_T9_ZBNlo")




