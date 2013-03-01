{-# LANGUAGE RecordWildCards #-}
module Anazump where

import Text.JSON
import Text.JSON.Types

data Order = Order {
  orderId :: String
}

instance JSON Order where
  readJSON (JSObject o) = return $ Order { .. }
    where orderId = grab o "order_id"

grab o s = case get_field o s of
  Nothing            -> error "Invalid field " ++ show s
  Just (JSString s') -> fromJSString s'
