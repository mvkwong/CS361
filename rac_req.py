import pandas as pd

class Recommender:
    def __init__(self, head_size, length, strung_weight, balance_type, balance_point) -> None:
        pref_head_size = float(head_size)
        pref_length = float(length)
        pref_strung_weight = float(strung_weight)
        if balance_point != 0:
            if balance_type == "Head light":
                pref_balance = abs(float(balance_point))
            elif balance_type == "Head heavy":
                pref_balance = -abs(float(balance_point))
            else:
                pref_balance = 0
        else:
            pref_balance = 0
        self.pref_list = [pref_head_size, pref_length, pref_strung_weight, pref_balance]
        self.df = pd.read_csv('cleaned_racquet_data.csv')

    #Create racquet shortlist based on immutable specs (head size, length)
    def create_shortlist(self):
        column_names = ['Racquet', 'Head Size (in)', 'Length', 'Strung Weight (g)', 'Balance']
        rac_shortlist = self.df[column_names]
        return rac_shortlist

    #Calc Euclidean distance score for each racquet by comparing each specification value against user pref
    def calc_scores(self, rac_shortlist):
        sim_score_list = []
        for i in range(len(rac_shortlist.index)):
            similarity_score = 0
            for j in range(1, len(rac_shortlist.columns)):
                similarity_score += (abs(self.pref_list[j-1] - rac_shortlist.loc[i, rac_shortlist.columns[j]]))**2
            similarity_score = similarity_score**0.5
            sim_score_list.append([similarity_score, rac_shortlist.loc[i, rac_shortlist.columns[0]]])
        sim_score_list.sort()
        return sim_score_list

    def get_recs(self):
        shortlist = self.create_shortlist()
        score_list = self.calc_scores(shortlist)
        result = []
        for i in range(min(5, len(score_list))):
            result.append(score_list[i][1])
        print(score_list[0])
        return result

    def export_csv(self):
        self.df.to_csv('Top 5 Racquet Recommendations.csv')
"""
head_size = 100
length = 27
strung_weight = 300
balance_type = 'balanced'
balance_point = 0
Recc = Recommender(head_size, length, strung_weight, balance_type, balance_point)
print(Recc.get_recs())"""