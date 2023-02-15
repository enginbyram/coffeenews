import newspaper

birgun_news = 'http://birgun.net'
sol_news = 'http://haber.sol.org.tr'

birgun_paper = newspaper.build(birgun_news)
sol_paper = newspaper.build(sol_news)
print(birgun_paper.size())
print(sol_paper.size())
