from numpy import maximum
import folium
import webbrowser

def main(coordPoints):
    print("======Generating Map...======")

    if(len(coordPoints)>0):
        freq = {}
        latMean = 0
        lonMean = 0
        for item in coordPoints:
            latMean += item[0]
            lonMean += item[1]
            loc = (item[0],item[1],item[2])
            if (loc in freq):
                freq[loc] = (maximum(item[3],freq[loc][0]),maximum(item[4],freq[loc][1]),maximum(item[5],freq[loc][2]))
            else:
                freq[loc] = (item[3],item[4],item[5])

        latMean /= len(coordPoints)
        lonMean /= len(coordPoints)


        casualtyMap = folium.Map(location=[latMean, lonMean], zoom_start=7, control_scale=True)

        for key, value in freq.items():
            folium.Marker([key[0],key[1]],popup=key[2]+": "+str(value[0])+" Deaths, "+str(value[1])+" Injuries, "+str(value[2])+" Missings").add_to(casualtyMap)

        casualtyMap.save("casualtyMap.html")
        webbrowser.open("casualtyMap.html")
    else:
        print("no information found")
