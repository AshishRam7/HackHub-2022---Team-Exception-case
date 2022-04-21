from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import smtplib
from email.message import EmailMessage


# Create your views here.


def home(request):

    return render(request, 'home.html', {'name': 'Ashish'})


def add(request):

    soil = str(request.POST['soil'])
    month = str(request.POST['month'])
    ph = float(request.POST['ph'])
    temp = float(request.POST['temp'])
    rainfall = float(request.POST['rainfall'])

    soils_for_each_crop = {

        # soil suitable for paddy:
        'paddy': [
            'sand loamy',
            'silty loam',
            'clay loamy',
            'silty'
        ],

        # soil suitable for wheat:
        'wheat': [
            'loamy',
            'clay loamy'
        ],
        # soil suitable for cotton:
        'cotton': [
            'alluvial',
            'clayey',
            'red loamy'],

        # soil suitable for maize:
        'maize': [
            'alluvial',
            'clay loamy',
            'red loamy',
            'clay loamy',
            'sand loamy'],

        # soil suitable for jowar:
        'jowar': [
            'sand loamy'
        ],
    }

    crops = {
        'paddy': 0,
        'wheat': 0,
        'cotton': 0,
        'maize': 0,
        'jowar': 0,
    }

    paddy = 0
    wheat = 0
    cotton = 0
    maize = 0
    jowar = 0

    # paddy_ph = [6, 7]
    # paddy_ph = [6, 7]
    # paddy_ph = [6, 7]
    # paddy_ph = [6, 7]
    # paddy_ph = [6, 7]

    for i in soils_for_each_crop:
        if soil in soils_for_each_crop[i]:
            crops[i] += 1
        else:
            crops[i] -= 5

    # print(crops)

    # print(crops)

    month_for_each_crop = {

        # sowing month suitable for paddy:
        'paddy': [
            'kharif'
        ],

        # month suitable for wheat:
        'wheat': [
            'rabi'
        ],

        # month suitable for cotton:
        'cotton': [
            'kharif'
        ],

        # month suitable for maize:
        'maize': [
            'kharif',
            'rabi'
        ],

        # month suitable for jowar:
        'jowar': [
            'kharif',
            'rabi'
        ],
    }

    for i in month_for_each_crop:
        if month in month_for_each_crop[i]:
            crops[i] += 1
        else:
            crops[i] -= 5

    '''
    if ph>=5 and ph<=9.5:
    paddy+= 1
    if ph>=6 and ph<=7:
        wheat+=1
        maize+=1
        cotton+=1
        jowar+=1
    elif ph<6 and ph>=5.5:
        maize+=1
    elif ph>7 and ph<=7.5:
        jowar+=1
        maize+=1
    elif ph>7.5 and ph<=8:
        cotton+=1
    '''

    # checking for ph level of soil

    if ph >= 6 and ph <= 7:
        wheat += 1
        maize += 1
        cotton += 1
        paddy += 1
        jowar += 1

    elif ph <= 5.5 and ph < 6:
        maize += 1
        paddy += 1

    elif ph >= 5 and ph < 5.5:
        paddy += 1

    elif ph > 7 and ph <= 7.5:
        paddy += 1
        jowar += 1
        maize += 1
        cotton += 1

    elif ph > 7.5 and ph <= 8:
        paddy += 1
        cotton += 1

    elif ph > 8 and ph <= 9.5:
        paddy += 1

    # paddy final

    # wheat final

    '''for i in crops:
    crops[i]+=paddy
    '''

    # print(crops)

    # jowar(kharif)- 6 to 7.5
    # jowar(rabi)- 6 to 7.5
    # paddy - 5 to 9.5
    # maize(kharif)- 5.5 to 7.5
    # maize(rabi)-5.5 to 7.5
    # cotton - 6 to 8
    # wheat -6 to 7

    # temperature checking:

    if temp >= 25 and temp <= 30:
        cotton += 1
        paddy += 1
        jowar += 1
        maize += 1

    elif temp >= 21 and temp < 25:
        wheat += 1
        cotton += 1
        paddy += 1

    elif temp > 30 and temp <= 32:
        cotton += 1
        jowar += 1

    elif temp >= 25 and temp <= 30:
        cotton += 1
        paddy += 1
        jowar += 1
        maize += 1

    elif temp >= 21 and temp < 25:
        wheat += 1
        cotton += 1
        paddy += 1

    elif temp > 30 and temp <= 32:
        cotton += 1
        jowar += 1

    # jowar(kharif)-25°C - 32°C
    # paddy - 16-30° C
    # maize-25°C - 30°C
    # cotton - 15-35°C
    # wheat -21-26°C

    # checking rainfall:
    if rainfall >= 20 and rainfall <= 40:
        jowar += 1
        wheat += 1

    elif rainfall > 20 and rainfall <= 75:
        wheat += 1

    elif rainfall > 50 and rainfall <= 100:
        cotton += 1
        maize += 1

    elif rainfall > 100:
        paddy += 1

    elif rainfall >= 21 and rainfall < 25:
        wheat += 1
        cotton += 1
        paddy += 1

    elif rainfall > 30 and rainfall <= 32:
        cotton += 1
        jowar += 1

    #print(paddy,wheat,cotton, maize, jowar)

    # jowar(kharif)- 20 cm - 40cm
    # paddy - 100 cm - 200 cm
    # maize(kharif) - 50 cm - 100 cm
    # cotton - 55 cm - 100 cm
    # wheat - 20 - 75cm
    # paddy final
    crops['paddy'] += paddy
    crops['wheat'] += wheat
    crops['jowar'] += jowar
    crops['maize'] += maize
    crops['cotton'] += cotton

    # print(crops)

    # max=0
    # for i in crops:
    #   if crops[i]>max:
    #       max+=crops[i]

    # print(max)
    # wheat final

    res = max(crops, key=crops.get)

    email = request.user.email
    first_name = request.user.first_name
    print(email)

    # with open("../templates/result.html") as f:
    #     content = f.read(}

    if res == 'wheat':
        textInHtml = '''<div>

      <h1>Wheat</h1>
      <h2>LAND PREPARATION<br />
        After harvest of previous crop, the field should be ploughed with disc or mould board plough. Field is usually
        prepared by giving one deep plough with iron plough followed by two or three times local plough and planking.
        Carried out plough in evening time and kept furrow open whole night to absorb some moisture from dew. Planking
        should be done after each plough early in the morning.

        SOWING<br />
        Time of sowing:<br />
        Wheat must be sown at the optimum time. Delayed sowing causes a gradual decline in the yield of wheat. The time
        of sowing is 25 October – November.<br />
        Spacing:<br />
        For normal sown crop a spacing of 20 - 22.5 cm between rows is recommended. When sowing is delayed a closer
        spacing of 15-18 cm should be adopted.<br />
        Broadcasting method<br />

        Sowing depth:<br />
        The sowing depth should be 4-5 cm.

        IRRIGATION<br />
        Recommended time of irrigations is as below in the table:
        <table>
          <tr>
            <th>Number of irrigations</th>
            <th>1st irrigation</th>
            <th>2st irrigation</th>
            <th>3st irrigation</th>
            <th>4st irrigation</th>
            <th>5st irrigation</th>

            <th>6st irrigation</th>
          <tr>
            <th>Interval of sowing</th>
            <th>20-25 days</th>
            <th>40-45 days</th>
            <th>60-65 days</th>
            <th>80-85 days</th>
            <th>100-105 days</th>
            <th>110-120 days</th>

          </tr>
          </tr>
        </table>




        <br />HARVESTING<br />
        Harvesting of high yielding dwarf variety is carried out when leaves and stem turn yellow and become fairly dry.
        To avoid loss in yield crop should be harvested before it is dead ripe. Timely harvesting is needed for optimum
        quality and consumer acceptance. The right stage for harvesting is when moisture in grain reaches to 25-30%. For
        manual harvesting use serrate edge sickles. Combines harvester are also available which can do harvesting,
        threshing and winnowing of wheat crop in single operation
      </h2>
      <div class="">
        <h2>

        </h2>

      </div>'''
        # email_alert("Hey", content, email)

    elif res == 'maize':
        textInHtml = '''<div class="paddy">
        <h1>Maize</h1>
        <h2>LAND PREPARATION<br />
          For cultivation selected land should be free from weeds and remains of previously grown crop. Plough the land
          to bring the soil to fine tilth. It may take 6 to 7 plough. Apply 4-6 tons/acre of well decomposed cow dung
          across the field, also apply 10 Azospirillum packets in field. Prepared furrow and ridges with 45 cm to 50 cm
          spacing.


          SOWING<br />
          Time of sowing:<br />
          In kharif season, crop is sown in month of May end to June corresponding with the onset of monsoon. Spring
          crops are sown during late February to end of march. Plantation of baby corn can be done all the year round,
          except December and January. Kharif and rabi season are best for sweet corn sowing.
          <br />
          Spacing:<br />
          To obtain higher yield along with resource-use efficiency, optimum plant spacing is the key factor.<br>
          1) For kharif maize : use spacing of 60x20 cm.<br>
          2) Sweet corn : use spacing of 60x20 cm spacing.<br>
          3) Baby corn: Use 60x20 cm or 60x15 cm spacing.<br>
          4) Pop corn: Use 50x15 cm spacing.<br>
          5) Fodder: use spacing of 30x10 cm spacing<br>
          <br>

          Sowing depth:<br />
          Seed should be sown at depth of 3-4 cm. For sweet corn cultivation keep depth of sowing to 2.5 cm.<br /><br />
          Method of sowing<br><Br>
          Sowing can be done manually by dibbling seeds or by mechanically with help of tractor drawn ridger seed drill.


          IRRIGATION<br />
          Keep field flooded up to two weeks after transplanting. When all water gets infiltrated two day after apply
          irrigation in field. Depth of standing water should not exceed 10 cm. While doing intercultural and weeding
          operation, drain out excess water from field and irrigate field after completion of this operations. Stop
          irrigation about a fortnight before maturity to facilitate easy harvesting.<br /><br />


          Fertilizer Requirement (kg/acre)<br />
          <table>

            <tr>
              <th>UREA</th>
              <th>DAP</th>
              <th>MOP</th>
              <th>SSP</th>
              <th>ZINC</th>
            </tr>
            <tr>
              <th>75 -110</th>
              <th>27-55</th>
              <th>75-150</th>
              <th>15-20</th>
              <th>8</th>
            </tr>
          </table>

          <br />Nutrient Requirement (kg/acre)<br />
          <table>

            <tr>
              <th>NITROGEN</th>
              <th>PHOSPHORUS</th>
              <th>POTASH</th>

            </tr>
            <tr>
              <th>35-50</th>
              <th>12-24</th>
              <th>8-12</th>

            </tr>
          </table><br>
          Irrigation<br>
          Apply irrigation immediately after sowing. Based upon soil type, on third or fourth day give lifesaving
          irrigation. In rainy season, if rain is satisfactory then it is not needed. Avoid water stagnation in early
          phase of crop and provide good drainage facility. Crop required less irrigation during early stage, 20 to 30
          days after sowing afterwards it required irrigation once in a week. Seedling, knee height stage, flowering and
          grain feeling are the most sensitive stage for irrigation. Water stress at this stage cause huge loss in
          yield. In case of water scarcity, irrigate alternate furrow. It will save water also.
          <br><br>



          <br />HARVESTING<br />
          Harvesting should be done when cobs outer cover turns from green to white. The optimum time of harvesting
          maize is when the stalks have dried and moisture of grain as about 17-20%. Drying place or equipment should be
          dry, clean and disinfected.'''
        # email_alert("Hey", content, email)

    elif res == 'paddy':
        textInHtml = '''<div class="paddy">
    <h1>Paddy</h1>
    <h2>LAND PREPARATION<br />
      After harvesting of wheat grow dhaincha (seed rate 20 kg/acre) or sunhemp @ 20 kg/acre or cowpea @ 12 kg/acre up
      to first week of May. When crop is of 6-8 week old, bury them into the soil one day before transplanting of paddy.
      It will save 25 kg of N per acre. Use laser land leveler for land levelling. After then puddle soil and to
      obtained fine well levelled puddle field to reduce water loss through percolation.<br />
      Seed Rate:<br />
      8kg seeds are sufficient for planting in one acre land.<br /><br />

      Seed treatment:<br />
      Before sowing, soak them in 10 Ltr water containing, Carbendazim@20gm+ Streptocycline@1gm for 8 to 10 hour before
      sowing. After then dry seeds in shade. And then use for sowing.
      Also you can use below mention fungicides to protect crop from root rot disease. Use chemical fungicides first
      then treat seed with Trichoderma<br /><br />

      SOWING<br />
      Time of sowing:<br />
      20 may to 5 june is the optimum time for sowing<br />
      Spacing:<br />
      For normal sown crop a spacing of 20 - 22.5 cm between rows is recommended. When sowing is delayed a closer
      spacing of 15-18 cm should be adopted.<br /><br />
      Method of sowing:<br />
      Broadcasting method<br />

      Sowing depth:<br />
      The seedlings should be transplanted at 2 to 3 cm depth. Shallow planting gives better yields.<br /><br />

      IRRIGATION<br />
      Keep field flooded up to two weeks after transplanting. When all water gets infiltrated two day after apply
      irrigation in field. Depth of standing water should not exceed 10 cm. While doing intercultural and weeding
      operation, drain out excess water from field and irrigate field after completion of this operations. Stop
      irrigation about a fortnight before maturity to facilitate easy harvesting.<br /><br />


      Fertilizer Requirement (kg/acre)<br />
      <table>

        <tr>
          <th>UREA</th>
          <th>DAP</th>
          <th>MOP</th>
          <th>SSP</th>
          <th>ZINC</th>
        </tr>
        <tr>
          <th>110</th>
          <th>27</th>
          <th>75</th>
          <th>20</th>
          <th>-</th>
        </tr>
      </table>

      <br />Nutrient Requirement (kg/acre)<br />
      <table>

        <tr>
          <th>NITROGEN</th>
          <th>PHOSPHORUS</th>
          <th>POTASH</th>

        </tr>
        <tr>
          <th>50</th>
          <th>12</th>
          <th>12</th>

        </tr>
      </table>



      <br />HARVESTING<br />
      Reap the yield once the panicles are developing fully as well as the crops get changed significantly yellow. The
      yield is generally harvested manually by sickles or by blend harvester. The harvested crops, tied up into compact
      bundles, strike it against really hard surface to split the grains from straw, accompanied by winnowing.<br />

    </h2>
    <div class="">
      <h2>

      </h2>

    </div>'''
        # email_alert("Hey", content, email)

    elif res == 'cotton':
        textInHtml = '''<div class="paddy">
            <h1>Cotton</h1>
            LAND PREPARATION<br />
            It required thorough land preparation for good germination and growth of crop. After removal of Rabi crop,
            irrigate field immediately then take ploughing of land with MB plough and planking. Carry out deep ploughing
            once in three years, it will help to keep check on perennial weeds also kill various soil borne pest and
            diseases
            Seed treatment:<br />
            Before sowing, soak them in 10 Ltr water containing, Carbendazim@20gm+ Streptocycline@1gm for 8 to 10 hour
            before sowing. After then dry seeds in shade. And then use for sowing.
            Also you can use below mention fungicides to protect crop from root rot disease. Use chemical fungicides
            first then treat seed with Trichoderma<br /><br />

            SOWING<br />
            Time of sowing:<br />
            Optimum time for sowing is in April - mid May. For Management of Mealybug, sow Bajra, Arhar, Maize and Jowar
            in the fields surrounding cotton crop. Avoid growing tur, moong and bhendi in and around cotton field as
            these harbour insect pests. In Punjab cotton wheat rotation is common but rotation with berseem and
            clusterbean has been found to have beneficial effect on the succeeding cotton crop.<br />
            Spacing:<br />
            For normal sown crop a spacing of 20 - 22.5 cm between rows is recommended. When sowing is delayed a closer
            spacing of 15-18 cm should be adopted.<br /><br />
            Method of sowing:<br />
            For sowing use seed drill for desi cotton while dibbling of seed is done in case of hybrids and Bt cotton.
            Square planting is beneficial compared to rectangular planting. Few gaps arise due to failure of seed
            germination and mortality of seedling. To overcome this gap filling is necessary. Two weeks after sowing the
            weak/diseased/damaged seedlings should be removed by keeping a healthy seedling/hill.<br>
            Broadcasting method<br />
            For American cotton use spacing of 75x15 cm under irrigated condition while under rain fed condition use
            spacing of 60x30 cm. For desi cotton use spacing of 60x30 cm for rain fed as well as for irrigated
            condition.
            Sowing depth:<br />
            Sowing should be done at depth of 5 cm.
            <br>

            IRRIGATION<br />
            Keep field flooded up to two weeks after transplanting. When all water gets infiltrated two day after apply
            irrigation in field. Depth of standing water should not exceed 10 cm. While doing intercultural and weeding
            operation, drain out excess water from field and irrigate field after completion of this operations. Stop
            irrigation about a fortnight before maturity to facilitate easy harvesting.<br /><br />


            Fertilizer Requirement (kg/acre)<br />
            <table>

              <tr>
                <th>Variable</th>
                <th>UREA</th>
                <th>DAP</th>
                <th>MOP</th>
                <th>SSP</th>
                <th>ZINC</th>
              </tr>
              <tr>
                <th>Bt</th>
                <th>65</th>
                <th>27</th>
                <th>75</th>
                <th>20</th>
                <th>-</th>
              </tr>
              <tr>
                <th>Non Bt</th>
                <th>130</th>
                <th>27</th>
                <th>75</th>
                <th>20</th>
                <th>-</th>
              </tr>

            </table>




            <br />HARVESTING<br />
            Picking of bolls should be done when bolls are fully mature. Avoid picking of wet bolls, pick cotton free
            from dry leaves trash. Damaged boll should be picked separately and discarded for seed purpose. The first
            and last picking are usually of low quality and should not be mixed with rest of the produce to fetch better
            price. Pick boll should be clean and dry to get good price. Do picking when there is no dew. Picking should
            be regularly done after every 7-8 days to avoid losses incurred due to fall of the cotton on ground. Delay
            in picking leads to falling of cotton on the ground which results in deterioration of quality. Harvest the
            American cotton at the interval of 15-20days and Desi cotton at 8-10 days interval. The picked kapas should
            be properly cleaned before taking to the market for sale.<br>'''
        # email_alert("Hey", content, email)

    elif res == 'jowar':
        textInHtml = '''<div class="paddy">
              <h1>Jowar</h1>
              <h2>
                LAND PREPARATION<br />
                Give one deep ploughing every year in shallow to medium deep soil. Give one to two ploughing followed by
                2 criss-cross harrowing. Prepare land in such a way that water stagnation will not occurrs in field.
                SOWING<br />
                Time of sowing:<br />
                Optimum time for sowing is from Mid-June to Mid -July. For early green fodder, carryout sowing from
                middle of March.
                <br />
                Spacing:<br />
                For sowing use spacing of "45 cm x 15 cm" or "60 cm x10 cm".
                <br /><br />
                Method of sowing:<br />
                In North India, sorghum is sown either by broadcast or sown in rows behind the plough.<br><br>


                Sowing depth:<br />
                Seed should not be sown more than 2-3 cm depth.<br>

                IRRIGATION<br />
                To get good yield, give proper irrigation at important stages like tillering, flowering and grain
                formation stages. These are critical stages for irrigation. In kharif season it required one to three
                irrigation depending upon rainfall intensity. Under adequate water supply in rabi and summer season,
                irrigation should be given at all these critical stages. If water is available for 2 irrigation only,
                these should be applied at flower primordial initiation and flowering stages

                Fertilizer Requirement (kg/acre)<br />
                <table>

                  <tr>
                    <th>UREA</th>
                    <th>DAP</th>
                    <th>MOP</th>
                    <th>SSP</th>
                    <th>ZINC</th>
                  </tr>
                  <tr>
                    <th>44</th>
                    <th>-</th>
                    <th>16</th>
                    <th>50</th>
                    <th>-</th>
                  </tr>
                </table>

                <br />Nutrient Requirement (kg/acre)<br />
                <table>

                  <tr>
                    <th>NITROGEN</th>
                    <th>PHOSPHORUS</th>
                    <th>POTASH</th>

                  </tr>
                  <tr>
                    <th>20</th>
                    <th>8</th>
                    <th>10</th>

                  </tr>
                </table>



                <br />HARVESTING<br />
                The right time for harvest is when grains become hard and contain less than 25% moisture. Once crop gets
                mature, harvest it immediately. For harvesting sickles are used. The plants are cut from near the ground
                level. After then stalks are tied into bundles of convenient sizes and stacked on threshing floor. After
                two to three days removed ear heads from plants. In some cases only ear heads are removed from standing
                crop and collected at threshing floor. After then they are sun dry for 3-4 days.
              </h2>


            </div>'''
        # email_alert("Hey", content, email)

    final = '''<!DOCTYPE html>
<html lang="en" dir="ltr">

<head>
  <meta charset="utf-8">
  <title>Result page</title>
  <link rel="stylesheet" href="result.css">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <title>Agriculture</title>
  <img width="60" height="60" style="margin: 40px; border: 1px white;"
    src="data:image/jpeg;base64,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AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAf/2Q==" />
</head>

<body>

  <br>
  
  {}
  </body>

</html>'''.format(textInHtml.replace("\n", ""))

    temp = '''<style>
    body {
        display: flex;
        justify-content: center;
        width: 98%;
        height: 98vh;
        font-family: 'DM Sans', sans-serif;
        background-image: url("https://www.desktopbackground.org/download/2560x1440/2012/01/20/331174_gallery-for-light-green-leaves-backgrounds_2950x2094_h.jpg");
    }

    table {

      border-collapse: collapse;
      width: 100%;
    }

    td,
    th {
      border: 4px solid #dddddd;
      border-color: black;
      text-align: left;
      padding: 8px;
    }

    h1 {
      font-family: 'DM Sans', sans-serif;
    }

    h2 {
      font-family: 'DM Sans', sans-serif;
    }
  </style>'''

    return render(request, 'result.html', {'res': final})


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = 'agroxtech22@gmail.com'
    password = "".join(list(map(chr, list(map(
        int, '104.109.101.114.104.97.115.111.111.109.100.114.103.117.114.107'.split("."))))))
    msg['from'] = user

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()


def labs(request):
    return render(request, 'pricing.html')
