# SMC Indicator Test Cases
**Author:** Abdullahi Amir Umar (beenumarr)
**Last Updated:** 2025-04-05 20:16:32 UTC
**Version:** 1.0.0 Alpha

## 1. Market Structure Test Cases

### 1.1 Break of Structure (BOS)
| ID | Test Case | Expected Result | Validation Criteria |
|----|-----------|-----------------|-------------------|
| BOS-001 | Bullish BOS with volume confirmation | Signal generated | Volume > 20 SMA |
| BOS-002 | Bearish BOS with momentum alignment | Signal generated | RSI < 30 |
| BOS-003 | False BOS rejection | No signal | Price < Previous low |

### 1.2 Change of Character (CHoCH)
| ID | Test Case | Expected Result | Validation Criteria |
|----|-----------|-----------------|-------------------|
| CHoCH-001 | Bullish CHoCH after downtrend | Signal generated | New high formed |
| CHoCH-002 | Bearish CHoCH after uptrend | Signal generated | New low formed |
| CHoCH-003 | CHoCH with volume divergence | Warning signal | Volume decreasing |

### 1.3 Order Block Detection
| ID | Test Case | Expected Result | Validation Criteria |
|----|-----------|-----------------|-------------------|
| OB-001 | Bullish OB formation | OB marked | Range < ATR * 2 |
| OB-002 | Bearish OB with mitigation | OB removed | Price crosses OB |
| OB-003 | Multiple OB stacking | Strongest marked | Highest volume OB |

## 2. Indicator Performance Tests

### 2.1 Win Rate Validation
| Timeframe | Minimum Win Rate | Sample Size | Market Condition |
|-----------|-----------------|-------------|------------------|
| H4 | 80% | 100 trades | All conditions |
| H1 | 75% | 100 trades | Trending only |
| 15M | 70% | 100 trades | High volatility |

### 2.2 Risk-Reward Scenarios
| Scenario | Risk:Reward | Expected Win Rate | Required Samples |
|----------|-------------|-------------------|------------------|
| Conservative | 1:2 | 85% | 500 trades |
| Moderate | 1:3 | 75% | 750 trades |
| Aggressive | 1:5 | 65% | 1000 trades |

## 3. Edge Cases

### 3.1 Market Conditions
- Extreme volatility (VIX > 40)
- Low liquidity periods
- News impact scenarios
- Gap handling
- Weekend price gaps