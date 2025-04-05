#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SMC Indicator Data Validator
Author: Abdullahi Amir Umar (beenumarr)
Created: 2025-04-05 20:16:32 UTC
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
from datetime import datetime

class DataValidator:
    def __init__(self, config: Dict = None):
        self.config = config or self._default_config()
        
    def validate_dataset(self, data: pd.DataFrame) -> Tuple[bool, Dict]:
        """Validate a dataset against quality criteria."""
        results = {
            "missing_values": self._check_missing_values(data),
            "zero_volume": self._check_zero_volume(data),
            "spread_threshold": self._check_spread_threshold(data),
            "data_continuity": self._check_data_continuity(data),
            "timestamp_validity": self._check_timestamps(data)
        }
        
        is_valid = all(results.values())
        return is_valid, results
    
    def _check_missing_values(self, data: pd.DataFrame) -> bool:
        """Check for missing values in critical fields."""
        critical_fields = ['open', 'high', 'low', 'close', 'volume']
        return not data[critical_fields].isnull().any().any()
    
    def _check_zero_volume(self, data: pd.DataFrame) -> bool:
        """Check for zero volume candles."""
        return not (data['volume'] == 0).any()
    
    def _check_spread_threshold(self, data: pd.DataFrame) -> bool:
        """Validate spread is within acceptable range."""
        if 'spread' in data.columns:
            return not (data['spread'] > self.config['max_spread']).any()
        return True
    
    def _check_data_continuity(self, data: pd.DataFrame) -> bool:
        """Check for gaps in time series."""
        expected_diff = pd.Timedelta(minutes=self.config['timeframe_minutes'])
        actual_diff = data.index.to_series().diff()
        return not (actual_diff > expected_diff).any()
    
    def _check_timestamps(self, data: pd.DataFrame) -> bool:
        """Validate timestamp formatting and timezone."""
        return all(isinstance(ts, pd.Timestamp) for ts in data.index)
    
    @staticmethod
    def _default_config() -> Dict:
        return {
            "timeframe_minutes": 15,
            "max_spread": 0.0003,
            "min_volume": 100,
            "required_fields": [
                "timestamp", "open", "high", "low", 
                "close", "volume", "spread"
            ]
        }