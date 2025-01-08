# a) Nick Blexrud 
# b) status = Complete 
# c) This program is built to inform the end user (YouTube Content Creator) of the types of ads to display 
# and when to pause or resume monitization based on the view count and the engagement rate, and
# to make a simple prediction of ad revenue

# set named constants
SKIPPABLE_AD_REV_PER_VIEW = .01
NON_SKIPPABLE_AD_REV_PER_VIEW = .15
VIDEO_VIEWS_LOW_THRESHOLD = 1000
VIDEO_VIEWS_HIGH_THRESHOLD = 5000
ENGAGEMENT_LOW_THRESHOLD = 2
NO_REVENUE = 0

# set end user input values as ints
video_views_last_30_days = int(input("Enter the number of views in the last 30 days: "))
engagment_rate = int(input("Enter the engagement rate percentage: "))

if video_views_last_30_days < VIDEO_VIEWS_LOW_THRESHOLD:
    monetization_strategy = "Do not display any ads."
    total_potential_revenue = NO_REVENUE
elif video_views_last_30_days >= VIDEO_VIEWS_LOW_THRESHOLD and video_views_last_30_days < VIDEO_VIEWS_HIGH_THRESHOLD:
    monetization_strategy = "Display only 'Skippable' ads."
    # calculate skippable revenue by multiplying SKIPPABLE_AD_REV_PER_VIEW by video_views_last_30_days
    calculate_skippable_revenue = SKIPPABLE_AD_REV_PER_VIEW * video_views_last_30_days
    total_potential_revenue = calculate_skippable_revenue
elif engagment_rate > ENGAGEMENT_LOW_THRESHOLD:
    monetization_strategy = "Display both 'Skippable' and 'Non-Skippable' ads."
    # calculate skippable revenue by multiplying SKIPPABLE_AD_REV_PER_VIEW by video_views_last_30_days
    calculate_skippable_revenue = SKIPPABLE_AD_REV_PER_VIEW * video_views_last_30_days
    # calculate non-skippable revenue by multiplying NON_SKIPPABLE_AD_REV_PER_VIEW by video_views_last_30_days
    calculate_non_skippable_revenue = NON_SKIPPABLE_AD_REV_PER_VIEW * video_views_last_30_days
    # sum skippable and non-skippable revenue
    total_potential_revenue = calculate_skippable_revenue + calculate_non_skippable_revenue
else:
    monetization_strategy = "Pause monetization for that video."
    total_potential_revenue = NO_REVENUE

print(f"Monetization Strategy: {monetization_strategy}")

# check if we have revenue, if we do then print message
if total_potential_revenue > 0: print(f"Total Potential Revenue: ${total_potential_revenue:,.2f}")