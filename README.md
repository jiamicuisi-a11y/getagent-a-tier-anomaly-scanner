# Bitget A-Tier Anomaly Scanner

This repo is a standalone GetAgent Playbook package for the Bitget A-tier anomaly scanner.

- GitHub repo: https://github.com/jiamicuisi-a11y/getagent-a-tier-anomaly-scanner
- Live demo: http://56.155.138.109/quant

It scans liquid Bitget perpetual contracts, ranks anomaly candidates, and emits signal-only output for review. The package is intentionally kept at the repository root so GetAgent Studio can import it without extra nesting.

## What it tries to capture

The scanner is trying to catch a fresh move that is backed by participation and trader pressure, not just a random candle. When the market is broadening participation and price is moving in the same direction as aggressive flow, that setup is treated as more interesting. When participation expands but price and sell pressure disagree, the strategy may lean short. If the evidence is mixed, it stays cautious and emits watch context rather than acting.

## Entry logic

A long signal is preferred when the market shows expanding participation, positive price behavior, and stronger buy-side pressure. A short signal is preferred when participation grows while price behavior and sell-side pressure lean the other way. The scanner is selective: it ranks the strongest aligned candidates and ignores weaker noise. Raising the minimum score makes the strategy more selective. Lowering it increases frequency but also allows more false positives.

## Exit and risk logic

The companion dashboard version of this strategy uses a fixed stop, a fixed reward target, cooldown after a closed position, and a limit on simultaneous exposure. That keeps risk from growing without control. In this GetAgent Playbook, the output is signal-only, so the platform can review the suggested direction and risk context before any separate trading action. The risk parameters are there to describe the intended behavior of the signal, not to promise a return.

## How to read the tunable parameters

The scanned contract universe controls breadth. A broader set can find more opportunities, while a tighter set focuses on deeper liquidity. The minimum score controls selectivity. The risk and stop settings define how conservative the idea is. A smaller risk setting makes the strategy more defensive; a larger one makes each idea more aggressive. The leverage setting describes the reference intensity of the original dashboard logic.

## Main risks

This strategy can underperform in choppy markets, thin liquidity, exchange-specific data gaps, and sudden news shocks. It can also struggle when open interest rises for hedging rather than directional conviction, or when price moves are too noisy for the scanner to separate signal from randomness. As with any trading idea, a paper result or a historical snapshot is not a guarantee of future performance.
