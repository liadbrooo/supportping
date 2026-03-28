from .supportping import SupportPing

def setup(bot):
    """Cog laden"""
    bot.add_cog(SupportPing(bot))
