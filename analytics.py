from collections import defaultdict

analytics_data = defaultdict(int)

def log_prediction(label, mode):
    analytics_data["total"] += 1
    analytics_data[label] += 1
    analytics_data[mode] += 1

def get_analytics():
    return {
        "total": analytics_data["total"],
        "Low Quality": analytics_data["Low Quality"],
        "Average Quality": analytics_data["Average Quality"],
        "High Quality": analytics_data["High Quality"],
        "Data Only": analytics_data["Data Only"],
        "Image Only": analytics_data["Image Only"],
        "Data + Image": analytics_data["Data + Image"],
    }
