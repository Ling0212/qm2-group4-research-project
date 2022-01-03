# KENDALL RANK CORRELATION COEFFICIENT IN PYTHON
# We ground ourselves on the definition of the Kendall-τ, in order to create the lines of code that will compute this coefficient. This τ is defined as:

τ = [(number of concordant pairs) - (number of dicordant pairs)] / [n(n - 1)/2]

# We say the pair (xi, yi) and (xj, yj) is concordant when i < j if, xi < xj and yi < yj. In the same way, this pair is concordant when i > j if, xi > xj and yi > yj. Otherwise, the pair is described as discordant.

# The following lines of code allow to compute the value of the Kendall-τ, previously defined:

def f_tau(liste,n):
    nb_dis=0    
    nb_conc=0
    for i in range(n):
        for j in range(i+1,n):
            if ( (liste[i][0] < liste[j][0]) and (liste[i][1] < liste[j][1]) ) or ( (liste[i][0] > liste[j][0]) and (liste[i][1] > liste[j][1]) ):
                nb_conc += 1
            if ( (liste[i][0] < liste[j][0]) and (liste[i][1] > liste[j][1]) ) or ( (liste[i][0] > liste[j][0]) and (liste[i][1] < liste[j][1]) ):
                nb_dis += 1
    tau = (nb_conc-nb_dis)/(1/2*n*(n-1))
    print (tau)

# The list we need to enter is written as associated 'pairs', corresponding to the x-value and y-value of each point. In our case, n is equal to 30 since we dispose of 30-years data for each variable. 
