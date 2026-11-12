#!/usr/bin/env python3
"""物联网设备上云数据量估算器

用途：FDE 现场摸底阶段快速估算数据量级，为网关选型、平台容量与带宽评估提供依据。
用法示例：
    python estimate_data_volume.py --devices 50 --points 20 --interval 5
    python estimate_data_volume.py --devices 3 --points 15 --interval 1 --payload 300

估算口径（均为估算值，需现场实测校准）：
    日消息数 = 设备数 x 点位数 x (86400 / 采样间隔)
    日数据量 = 日消息数 x 单条消息平均字节数
"""
import argparse


def fmt(n: float) -> str:
    """数字格式化：大数用万/亿中文单位更直观"""
    if n >= 1e8:
        return f"{n / 1e8:.2f} 亿"
    if n >= 1e4:
        return f"{n / 1e4:.1f} 万"
    return f"{n:,.0f}"


def main() -> None:
    parser = argparse.ArgumentParser(description="估算设备上云的日消息量、日数据量与平均带宽")
    parser.add_argument("--devices", type=int, required=True, help="设备/网关数量")
    parser.add_argument("--points", type=int, required=True, help="平均每设备采集点位数")
    parser.add_argument("--interval", type=float, required=True, help="采样间隔（秒）")
    parser.add_argument("--payload", type=int, default=200, help="单条消息平均字节数（默认 200）")
    args = parser.parse_args()

    if args.devices <= 0 or args.points <= 0 or args.interval <= 0:
        parser.error("--devices/--points/--interval 必须为正数")

    msgs_per_device_day = args.points * (86400 / args.interval)
    msgs_day = msgs_per_device_day * args.devices
    bytes_day = msgs_day * args.payload
    mb_day = bytes_day / 1e6
    gb_month = mb_day * 30 / 1000
    kbps_avg = bytes_day * 8 / 86400 / 1000  # 平均上行带宽（Kbps）

    print("=" * 56)
    print("物联网数据量估算结果（估算值，需现场实测校准）")
    print("=" * 56)
    print(f"输入参数      : 设备 {args.devices} 台 x {args.points} 点位，间隔 {args.interval}s，消息 {args.payload}B")
    print(f"单设备日消息数 : {fmt(msgs_per_device_day)} 条")
    print(f"日消息总数     : {fmt(msgs_day)} 条")
    print(f"日数据量       : {mb_day:,.1f} MB（约 {mb_day / 1024:.2f} GB）")
    print(f"月数据量       : {gb_month:,.1f} GB（按 30 天）")
    print(f"平均上行带宽   : {kbps_avg:,.1f} Kbps（峰值建议按 5-10 倍预留）")
    print("-" * 56)
    print("提示：断网缓存按日数据量 x 预期断网时长估算；时序库容量按月数据量 x 保留月数估算。")


if __name__ == "__main__":
    main()
