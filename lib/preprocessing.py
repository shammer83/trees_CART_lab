from sklearn.base import BaseEstimator, TransformerMixin
from scipy.stats import boxcox

class Deskew(BaseEstimator, TransformerMixin):
    #mM = MinMaxScaler(feature_range=( .5, 1.5))
    def __init__ (self,alpha=1):
        self.alpha = alpha
    def _reset(self):
        pass
    def fit(self,X,y=None):
        self
    def transform(self,X):
        #mM = MinMaxScaler(feature_range=( .5, 1.5))
        #mM.fit(X)
        #X_minMax = pd.DataFrame( mM.fit_transform(X))
        #X_minMax = mM.fit_transform(X)
        #X_minMax = pd.DataFrame( mM.fit_transform(X))
        #box_cox_df = pd.DataFrame()
        X += self.alpha
        boxed = list()
        lambdas = list()
        #for col in X_minMax.T:
        for col in X.T:
            boxcoxed, lam = boxcox( col)
            lambdas.append(lam)
            boxed.append( boxcoxed)
               

            #box_cox_df[col] = pd.Series( boxcoxed)
            #box_cox = box_cox_df.as_matrix()
        #return box_cox_df, lambdas
        box_cox = np.array( boxed).T
        return box_cox #, lambdas
    def fit_transform(self,X,y=None):
        return self.transform(X)
    def inverse_transform(self, X, lambdas):## Needs work
        X_s = pd.DataFrame()  ## Original skewed, non 0 centered or variance scaled
        for col, lam in zip(X.columns, lambdas):
            
            if lam != 0:
                reskewed_col = (lam*X[col] + 1)**(1/lam)
            else:
                reskewed_col = np.exp(X[col])
            X_s[col] = pd.Series( reskewed_col)
        X_o_s = pd.DataFrame( mM.inverse_transform(X_s))  ## descaled, deskewed data
        return X_o_s
        #return np.exp(X) - self.alpha
    def score(self,X,y):
        pass