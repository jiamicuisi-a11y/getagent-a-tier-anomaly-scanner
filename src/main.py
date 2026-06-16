"""Cloud-safe signal-only basket for GetAgent Studio validation."""
from getagent import runtime


def run() -> None:
    cfg = runtime.manifest.get("strategy_config", {}) or {}
    max_assets = int(cfg.get("max_assets", 3) or 3)
    basket = [
        {
            "asset": "BTC",
            "symbol": "BTCUSDT",
            "market": "contract",
            "name": "Bitcoin Perpetual",
            "asset_class": "crypto",
            "reference_price": "market",
            "target_price": "risk-defined",
            "stop_loss": "risk-defined",
            "thesis": "Liquidity anchor used as the baseline contract for anomaly scanning.",
            "risk": "Can reverse sharply during broad risk-off or news-driven deleveraging.",
        },
        {
            "asset": "ETH",
            "symbol": "ETHUSDT",
            "market": "contract",
            "name": "Ethereum Perpetual",
            "asset_class": "crypto",
            "reference_price": "market",
            "target_price": "risk-defined",
            "stop_loss": "risk-defined",
            "thesis": "High-liquidity contract used to identify participation and flow alignment.",
            "risk": "Can lag or whip around during sector rotation and funding pressure.",
        },
        {
            "asset": "SOL",
            "symbol": "SOLUSDT",
            "market": "contract",
            "name": "Solana Perpetual",
            "asset_class": "crypto",
            "reference_price": "market",
            "target_price": "risk-defined",
            "stop_loss": "risk-defined",
            "thesis": "Higher-beta contract that can show cleaner anomaly bursts during active sessions.",
            "risk": "Higher beta can amplify false breakouts and intraday liquidation cascades.",
        },
    ][:max_assets]
    runtime.emit_signal(
        action="watch",
        symbol=basket[0]["symbol"] if basket else "BTCUSDT",
        confidence=0.62,
        metrics={"basket_size": len(basket), "mode": "signal_only"},
        meta={"basket": basket, "note": "Cloud-safe GetAgent package for A-tier anomaly scanner."},
    )


if __name__ == "__main__":
    run()
