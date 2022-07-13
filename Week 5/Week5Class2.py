{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "37bddbe6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "url = \"https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data\"\n",
    "abalone = pd.read_csv(url, header=None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "694857b0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "      <th>3</th>\n",
       "      <th>4</th>\n",
       "      <th>5</th>\n",
       "      <th>6</th>\n",
       "      <th>7</th>\n",
       "      <th>8</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>M</td>\n",
       "      <td>0.455</td>\n",
       "      <td>0.365</td>\n",
       "      <td>0.095</td>\n",
       "      <td>0.5140</td>\n",
       "      <td>0.2245</td>\n",
       "      <td>0.1010</td>\n",
       "      <td>0.150</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>M</td>\n",
       "      <td>0.350</td>\n",
       "      <td>0.265</td>\n",
       "      <td>0.090</td>\n",
       "      <td>0.2255</td>\n",
       "      <td>0.0995</td>\n",
       "      <td>0.0485</td>\n",
       "      <td>0.070</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>F</td>\n",
       "      <td>0.530</td>\n",
       "      <td>0.420</td>\n",
       "      <td>0.135</td>\n",
       "      <td>0.6770</td>\n",
       "      <td>0.2565</td>\n",
       "      <td>0.1415</td>\n",
       "      <td>0.210</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>M</td>\n",
       "      <td>0.440</td>\n",
       "      <td>0.365</td>\n",
       "      <td>0.125</td>\n",
       "      <td>0.5160</td>\n",
       "      <td>0.2155</td>\n",
       "      <td>0.1140</td>\n",
       "      <td>0.155</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>I</td>\n",
       "      <td>0.330</td>\n",
       "      <td>0.255</td>\n",
       "      <td>0.080</td>\n",
       "      <td>0.2050</td>\n",
       "      <td>0.0895</td>\n",
       "      <td>0.0395</td>\n",
       "      <td>0.055</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   0      1      2      3       4       5       6      7   8\n",
       "0  M  0.455  0.365  0.095  0.5140  0.2245  0.1010  0.150  15\n",
       "1  M  0.350  0.265  0.090  0.2255  0.0995  0.0485  0.070   7\n",
       "2  F  0.530  0.420  0.135  0.6770  0.2565  0.1415  0.210   9\n",
       "3  M  0.440  0.365  0.125  0.5160  0.2155  0.1140  0.155  10\n",
       "4  I  0.330  0.255  0.080  0.2050  0.0895  0.0395  0.055   7"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "abalone.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "d402765f",
   "metadata": {},
   "outputs": [],
   "source": [
    "abalone.columns = [\"Sex\", \"Length\", \"Diameter\", \"Height\", \"Whole weight\", \"Shucked weight\", \"Viscera weight\", \"Shell weight\", \"Rings\",]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f8fad3cc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Sex</th>\n",
       "      <th>Length</th>\n",
       "      <th>Diameter</th>\n",
       "      <th>Height</th>\n",
       "      <th>Whole weight</th>\n",
       "      <th>Shucked weight</th>\n",
       "      <th>Viscera weight</th>\n",
       "      <th>Shell weight</th>\n",
       "      <th>Rings</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>M</td>\n",
       "      <td>0.455</td>\n",
       "      <td>0.365</td>\n",
       "      <td>0.095</td>\n",
       "      <td>0.5140</td>\n",
       "      <td>0.2245</td>\n",
       "      <td>0.1010</td>\n",
       "      <td>0.150</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>M</td>\n",
       "      <td>0.350</td>\n",
       "      <td>0.265</td>\n",
       "      <td>0.090</td>\n",
       "      <td>0.2255</td>\n",
       "      <td>0.0995</td>\n",
       "      <td>0.0485</td>\n",
       "      <td>0.070</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>F</td>\n",
       "      <td>0.530</td>\n",
       "      <td>0.420</td>\n",
       "      <td>0.135</td>\n",
       "      <td>0.6770</td>\n",
       "      <td>0.2565</td>\n",
       "      <td>0.1415</td>\n",
       "      <td>0.210</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>M</td>\n",
       "      <td>0.440</td>\n",
       "      <td>0.365</td>\n",
       "      <td>0.125</td>\n",
       "      <td>0.5160</td>\n",
       "      <td>0.2155</td>\n",
       "      <td>0.1140</td>\n",
       "      <td>0.155</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>I</td>\n",
       "      <td>0.330</td>\n",
       "      <td>0.255</td>\n",
       "      <td>0.080</td>\n",
       "      <td>0.2050</td>\n",
       "      <td>0.0895</td>\n",
       "      <td>0.0395</td>\n",
       "      <td>0.055</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Sex  Length  Diameter  Height  Whole weight  Shucked weight  Viscera weight  \\\n",
       "0   M   0.455     0.365   0.095        0.5140          0.2245          0.1010   \n",
       "1   M   0.350     0.265   0.090        0.2255          0.0995          0.0485   \n",
       "2   F   0.530     0.420   0.135        0.6770          0.2565          0.1415   \n",
       "3   M   0.440     0.365   0.125        0.5160          0.2155          0.1140   \n",
       "4   I   0.330     0.255   0.080        0.2050          0.0895          0.0395   \n",
       "\n",
       "   Shell weight  Rings  \n",
       "0         0.150     15  \n",
       "1         0.070      7  \n",
       "2         0.210      9  \n",
       "3         0.155     10  \n",
       "4         0.055      7  "
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "abalone.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "c3670cef",
   "metadata": {},
   "outputs": [],
   "source": [
    "abalone = abalone.drop(\"Sex\", axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "24d03bc9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Diameter</th>\n",
       "      <th>Height</th>\n",
       "      <th>Whole weight</th>\n",
       "      <th>Shucked weight</th>\n",
       "      <th>Viscera weight</th>\n",
       "      <th>Shell weight</th>\n",
       "      <th>Rings</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.455</td>\n",
       "      <td>0.365</td>\n",
       "      <td>0.095</td>\n",
       "      <td>0.5140</td>\n",
       "      <td>0.2245</td>\n",
       "      <td>0.1010</td>\n",
       "      <td>0.150</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.350</td>\n",
       "      <td>0.265</td>\n",
       "      <td>0.090</td>\n",
       "      <td>0.2255</td>\n",
       "      <td>0.0995</td>\n",
       "      <td>0.0485</td>\n",
       "      <td>0.070</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.530</td>\n",
       "      <td>0.420</td>\n",
       "      <td>0.135</td>\n",
       "      <td>0.6770</td>\n",
       "      <td>0.2565</td>\n",
       "      <td>0.1415</td>\n",
       "      <td>0.210</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.440</td>\n",
       "      <td>0.365</td>\n",
       "      <td>0.125</td>\n",
       "      <td>0.5160</td>\n",
       "      <td>0.2155</td>\n",
       "      <td>0.1140</td>\n",
       "      <td>0.155</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.330</td>\n",
       "      <td>0.255</td>\n",
       "      <td>0.080</td>\n",
       "      <td>0.2050</td>\n",
       "      <td>0.0895</td>\n",
       "      <td>0.0395</td>\n",
       "      <td>0.055</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Length  Diameter  Height  Whole weight  Shucked weight  Viscera weight  \\\n",
       "0   0.455     0.365   0.095        0.5140          0.2245          0.1010   \n",
       "1   0.350     0.265   0.090        0.2255          0.0995          0.0485   \n",
       "2   0.530     0.420   0.135        0.6770          0.2565          0.1415   \n",
       "3   0.440     0.365   0.125        0.5160          0.2155          0.1140   \n",
       "4   0.330     0.255   0.080        0.2050          0.0895          0.0395   \n",
       "\n",
       "   Shell weight  Rings  \n",
       "0         0.150     15  \n",
       "1         0.070      7  \n",
       "2         0.210      9  \n",
       "3         0.155     10  \n",
       "4         0.055      7  "
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "abalone.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "e1db4be4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Distribution of target variable\n",
    "import matplotlib.pyplot as plt\n",
    "abalone[\"Rings\"].hist(bins=15)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "621d4728",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Length            0.556720\n",
       "Diameter          0.574660\n",
       "Height            0.557467\n",
       "Whole weight      0.540390\n",
       "Shucked weight    0.420884\n",
       "Viscera weight    0.503819\n",
       "Shell weight      0.627574\n",
       "Rings             1.000000\n",
       "Name: Rings, dtype: float64"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Find out about correlations between the features and the target\n",
    "correlation_matrix = abalone.corr()\n",
    "correlation_matrix[\"Rings\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "3bf3f2ae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Diameter</th>\n",
       "      <th>Height</th>\n",
       "      <th>Whole weight</th>\n",
       "      <th>Shucked weight</th>\n",
       "      <th>Viscera weight</th>\n",
       "      <th>Shell weight</th>\n",
       "      <th>Rings</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Length</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.986812</td>\n",
       "      <td>0.827554</td>\n",
       "      <td>0.925261</td>\n",
       "      <td>0.897914</td>\n",
       "      <td>0.903018</td>\n",
       "      <td>0.897706</td>\n",
       "      <td>0.556720</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Diameter</th>\n",
       "      <td>0.986812</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.833684</td>\n",
       "      <td>0.925452</td>\n",
       "      <td>0.893162</td>\n",
       "      <td>0.899724</td>\n",
       "      <td>0.905330</td>\n",
       "      <td>0.574660</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Height</th>\n",
       "      <td>0.827554</td>\n",
       "      <td>0.833684</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.819221</td>\n",
       "      <td>0.774972</td>\n",
       "      <td>0.798319</td>\n",
       "      <td>0.817338</td>\n",
       "      <td>0.557467</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Whole weight</th>\n",
       "      <td>0.925261</td>\n",
       "      <td>0.925452</td>\n",
       "      <td>0.819221</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.969405</td>\n",
       "      <td>0.966375</td>\n",
       "      <td>0.955355</td>\n",
       "      <td>0.540390</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Shucked weight</th>\n",
       "      <td>0.897914</td>\n",
       "      <td>0.893162</td>\n",
       "      <td>0.774972</td>\n",
       "      <td>0.969405</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.931961</td>\n",
       "      <td>0.882617</td>\n",
       "      <td>0.420884</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Viscera weight</th>\n",
       "      <td>0.903018</td>\n",
       "      <td>0.899724</td>\n",
       "      <td>0.798319</td>\n",
       "      <td>0.966375</td>\n",
       "      <td>0.931961</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.907656</td>\n",
       "      <td>0.503819</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Shell weight</th>\n",
       "      <td>0.897706</td>\n",
       "      <td>0.905330</td>\n",
       "      <td>0.817338</td>\n",
       "      <td>0.955355</td>\n",
       "      <td>0.882617</td>\n",
       "      <td>0.907656</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.627574</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rings</th>\n",
       "      <td>0.556720</td>\n",
       "      <td>0.574660</td>\n",
       "      <td>0.557467</td>\n",
       "      <td>0.540390</td>\n",
       "      <td>0.420884</td>\n",
       "      <td>0.503819</td>\n",
       "      <td>0.627574</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                  Length  Diameter    Height  Whole weight  Shucked weight  \\\n",
       "Length          1.000000  0.986812  0.827554      0.925261        0.897914   \n",
       "Diameter        0.986812  1.000000  0.833684      0.925452        0.893162   \n",
       "Height          0.827554  0.833684  1.000000      0.819221        0.774972   \n",
       "Whole weight    0.925261  0.925452  0.819221      1.000000        0.969405   \n",
       "Shucked weight  0.897914  0.893162  0.774972      0.969405        1.000000   \n",
       "Viscera weight  0.903018  0.899724  0.798319      0.966375        0.931961   \n",
       "Shell weight    0.897706  0.905330  0.817338      0.955355        0.882617   \n",
       "Rings           0.556720  0.574660  0.557467      0.540390        0.420884   \n",
       "\n",
       "                Viscera weight  Shell weight     Rings  \n",
       "Length                0.903018      0.897706  0.556720  \n",
       "Diameter              0.899724      0.905330  0.574660  \n",
       "Height                0.798319      0.817338  0.557467  \n",
       "Whole weight          0.966375      0.955355  0.540390  \n",
       "Shucked weight        0.931961      0.882617  0.420884  \n",
       "Viscera weight        1.000000      0.907656  0.503819  \n",
       "Shell weight          0.907656      1.000000  0.627574  \n",
       "Rings                 0.503819      0.627574  1.000000  "
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "correlation_matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "6534bfd2",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Extract the data from the panda dataframe\n",
    "x = abalone.drop(\"Rings\", axis = 1) #Exclude the target\n",
    "x = x.values\n",
    "y = abalone[\"Rings\"] #Extract the data\n",
    "y = y.values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "247fb5e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Split the dataset using sklearn\n",
    "from sklearn.model_selection import train_test_split\n",
    "X_train, X_test, Y_train, Y_test = train_test_split(x, y, random_state = 12345, test_size=0.15)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "c9aec2ca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "KNeighborsRegressor(n_neighbors=3)"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Create a kNN regression model\n",
    "from sklearn.neighbors import KNeighborsRegressor\n",
    "knn_model = KNeighborsRegressor(n_neighbors = 3)\n",
    "knn_model.fit(X_train, Y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "4d47da35",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training score:  0.728628631885362\n",
      "Testing score:  0.49880767203391296\n"
     ]
    }
   ],
   "source": [
    "#Predict for training data and calculate prediction error (easier method)\n",
    "train_scores = knn_model.score(X_train, Y_train)\n",
    "test_scores = knn_model.score(X_test, Y_test)\n",
    "print(\"Training score: \", train_scores)\n",
    "print(\"Testing score: \", test_scores)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "6dfed905",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(4177, 7)"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "289fe34e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Predict for training data and calculate prediction error (other method - 1 haven't written the code yet)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
