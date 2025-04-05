#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SMC Indicator Performance Analyzer
Author: Abdullahi Amir Umar (beenumarr)
Created: 2025-04-05 20:16:32 UTC
"""

import pandas as pd
import numpy as np
from typing import Dict, List
from datetime import datetime
import plotly.graph_objects as go

class PerformanceAnalyzer:
    def __init__(self):
        self.required_win_rate = 0.80
        self.min_profit_factor = 2.0
        self.min_sharpe_ratio = 1.5
        
    def analyze_performance(self, results: pd.DataFrame) -> Dict:
        """Analyze trading performance metrics."""
        metrics = {
            "win_rate": self._calculate_win_rate(results),
            "profit_factor": self._calculate_profit_factor(results),
            "sharpe_ratio": self._calculate_sharpe_ratio(results),
            "max_drawdown": self._calculate_max_drawdown(results),
            "risk_adjusted_return": self._calculate_risk_adjusted_return(results),
            "expectancy": self._calculate_expectancy(results)
        }
        
        return self._validate_metrics(metrics)
    
    def _calculate_win_rate(self, results: pd.DataFrame) -> float:
        """Calculate win rate from trade results."""
        winning_trades = len(results[results['profit'] > 0])
        total_trades = len(results)
        return winning_trades / total_trades if total_trades > 0 else 0
    
    def _calculate_profit_factor(self, results: pd.DataFrame) -> float:
        """Calculate profit factor from trade results."""
        gross_profit = results[results['profit'] > 0]['profit'].sum()
        gross_loss = abs(results[results['profit'] < 0]['profit'].sum())
        return gross_profit / gross_loss if gross_loss != 0 else 0
    
    def _calculate_risk_adjusted_return(self, results: pd.DataFrame) -> float:
        """Calculate risk-adjusted return using advanced metrics."""
        returns = results['profit'].values
        volatility = np.std(returns) * np.sqrt(252)
        sharpe = self._calculate_sharpe_ratio(results)
        return sharpe * (1 - volatility)
    
    def _validate_metrics(self, metrics: Dict) -> Dict:
        """Validate performance metrics against required thresholds."""
        metrics['meets_criteria'] = (
            metrics['win_rate'] >= self.required_win_rate and
            metrics['profit_factor'] >= self.min_profit_factor and
            metrics['sharpe_ratio'] >= self.min_sharpe_ratio
        )
        return metrics