def ratingThreshold(ratings,threshold):
    ret_a = []
    for i in range(len(ratings)):
        if sum(ratings[i])/len(ratings[i]) < threshold:
            ret_a.append(i)
    return ret_a

print(ratingThreshold([[3,4],[3,3,3,4],[4]],3.5))