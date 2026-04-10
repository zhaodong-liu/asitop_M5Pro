def parse_thermal_pressure(powermetrics_parse):
    return powermetrics_parse["thermal_pressure"]


def parse_cpu_metrics(powermetrics_parse):
    p_core = []
    s_core = []
    cpu_metrics = powermetrics_parse["processor"]
    cpu_metric_dict = {}
    # cpu_clusters
    cpu_clusters = cpu_metrics["clusters"]
    for cluster in cpu_clusters:
        name = cluster["name"]
        # print(f"Parsing {name} metrics...")
        cpu_metric_dict[name+"_freq_Mhz"] = int(cluster["freq_hz"]/(1e6))
        cpu_metric_dict[name+"_active"] = int((1 - cluster["idle_ratio"])*100)
        for cpu in cluster["cpus"]:
            name = 'P-Cluster' if name.startswith("P") else 'S-Cluster'
            core = p_core if name.startswith("P") else s_core
            core.append(cpu["cpu"])
            cpu_metric_dict[name + str(cpu["cpu"]) + "_freq_Mhz"] = int(cpu["freq_hz"] / (1e6))
            cpu_metric_dict[name + str(cpu["cpu"]) + "_active"] = int((1 - cpu["idle_ratio"]) * 100)
    cpu_metric_dict["p_core"] = p_core
    cpu_metric_dict["s_core"] = s_core
    if "P-Cluster_active" not in cpu_metric_dict:
        p_active_vals = [v for k, v in cpu_metric_dict.items() if k.startswith("P") and k.endswith("_active")]
        cpu_metric_dict["P-Cluster_active"] = int(sum(p_active_vals) / len(p_active_vals)) if p_active_vals else 0
    if "P-Cluster_freq_Mhz" not in cpu_metric_dict:
        p_freq_vals = [v for k, v in cpu_metric_dict.items() if k.startswith("P") and k.endswith("_freq_Mhz")]
        cpu_metric_dict["P-Cluster_freq_Mhz"] = max(p_freq_vals) if p_freq_vals else 0
    if "S-Cluster_active" not in cpu_metric_dict:
        s_active_vals = [v for k, v in cpu_metric_dict.items() if k.startswith("S") and k.endswith("_active")]
        cpu_metric_dict["S-Cluster_active"] = int(sum(s_active_vals) / len(s_active_vals)) if s_active_vals else 0
    if "S-Cluster_freq_Mhz" not in cpu_metric_dict:
        s_freq_vals = [v for k, v in cpu_metric_dict.items() if k.startswith("S") and k.endswith("_freq_Mhz")]
        cpu_metric_dict["S-Cluster_freq_Mhz"] = max(s_freq_vals) if s_freq_vals else 0
    # power
    cpu_metric_dict["ane_W"] = cpu_metrics["ane_energy"]/1000
    #cpu_metric_dict["dram_W"] = cpu_metrics["dram_energy"]/1000
    cpu_metric_dict["cpu_W"] = cpu_metrics["cpu_energy"]/1000
    cpu_metric_dict["gpu_W"] = cpu_metrics["gpu_energy"]/1000
    cpu_metric_dict["package_W"] = cpu_metrics["combined_power"]/1000
    return cpu_metric_dict


def parse_gpu_metrics(powermetrics_parse):
    gpu_metrics = powermetrics_parse["gpu"]
    gpu_metrics_dict = {
        "freq_MHz": int(gpu_metrics["freq_hz"]),
        "active": int((1 - gpu_metrics["idle_ratio"])*100),
    }
    return gpu_metrics_dict
