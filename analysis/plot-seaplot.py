import seaborn as sns; sns.set(color_codes=True)
data = pd.read_csv('20180105-2.dataset')

ax = sns.pointplot(x="time", y="red", data=data)
