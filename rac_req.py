import pandas as pd

class Recommender:
    def __init__(self, head_size, length, strung_weight, balance_type, balance_point, brand) -> None:
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
        self.pref_list = [pref_head_size, pref_length, pref_strung_weight, pref_balance, brand]
        self.df = pd.read_csv('cleaned_racquet_data.csv')
        self.results_df = None

    #Create racquet shortlist based on immutable specs (head size, length)
    def create_shortlist(self):
        #column_names = ['Racquet', 'Head Size (in)', 'Length', 'Strung Weight (g)', 'Balance']
        column_names = ['Racquet', 'Head Size (in)', 'Length', 'Strung Weight (g)', 'Balance', 'Brand']
        rac_shortlist = self.df[column_names]
        return rac_shortlist

    #Calc Euclidean distance score for each racquet by comparing each specification value against user pref
    def calc_scores(self, rac_shortlist):
        sim_score_list = []
        for i in range(len(rac_shortlist.index)):
            similarity_score = 0
            racquet_brand = rac_shortlist.loc[i, 'Brand']
            pref_brand = self.pref_list[-1]
            if racquet_brand == pref_brand or pref_brand == 'Any Brand':
                for j in range(1, len(rac_shortlist.columns)-1):
                    similarity_score += (abs(self.pref_list[j-1] - rac_shortlist.loc[i, rac_shortlist.columns[j]]))**2
            else:
                similarity_score = 1000
            similarity_score = similarity_score**0.5
            sim_score_list.append([similarity_score])
            for j in range(len(rac_shortlist.columns)-1):
                sim_score_list[-1].append(rac_shortlist.loc[i, rac_shortlist.columns[j]])
        sim_score_list.sort()
        return sim_score_list

    def get_recs(self):
        shortlist = self.create_shortlist()
        score_list = self.calc_scores(shortlist)
        result = []
        for i in range(min(5, len(score_list))):
            result.append(score_list[i][1])
        self.create_results_df(score_list)
        return result

    def create_results_df(self, score_list):
        self.results_df = pd.DataFrame(score_list[0:5], columns=['Similarity Score', 'Racquet', 'Head Size (in)', 'Length', 'Strung Weight (g)', 'Balance (neg = head light)'])
        del self.results_df['Similarity Score']

    def export_csv(self):
        self.results_df.to_csv('Top 5 Racquet Recommendations.csv')