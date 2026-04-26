class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = "#username"
        self.password = "#password"
        self.login_btn = "text=Login"

    async def login(self, user, pwd):
        await self.page.fill(self.username, user)
        await self.page.fill(self.password, pwd)
        await self.page.click(self.login_btn)